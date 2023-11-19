from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

from .newsletter import first_opt_in, mailgun_handle_bounce, second_opt_in, unsubscribe


def is_ajax(request):
    print(request.META.get("HTTP_X_REQUESTED_WITH"))
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def handle_newsletter_subscribe(form, host):
    name = form.cleaned_data["subscriber_name"]
    email = form.cleaned_data["subscriber_email"]
    consented_at = datetime.utcnow().isoformat()
    consented_from = "NewsLetterSubscribeForm"
    confirm_url = "https://{}{}".format(host, reverse(newsletter_confirm))
    withdraw_url = "https://{}{}".format(host, reverse(newsletter_unsubscribe))
    return first_opt_in(name, email, consented_at, consented_from, confirm_url, withdraw_url)


def ajax_newsletter_subscribe(request):
    from home.forms import NewsletterSubscribeForm

    form = NewsletterSubscribeForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)
    else:
        result = handle_newsletter_subscribe(form, request.get_host())
        if result:
            return JsonResponse({"status": "confirmation sent"}, status=201)
        else:
            return JsonResponse({"status": "server error"}, status=500)


def newsletter_subscribe(request):
    from home.forms import NewsletterSubscribeForm

    if request.method == "POST":
        return ajax_newsletter_subscribe(request)
    else:
        form = NewsletterSubscribeForm()
    return render(
        request,
        "home/newsletter_subscribe.html",
        {
            "subscribe_page_url": reverse(newsletter_subscribe),
            "unsubscribe_page_url": reverse(newsletter_unsubscribe),
            "form": form,
        },
    )


def newsletter_confirm(request):
    code = request.GET["code"]
    email = request.GET["subscriber_email"]
    result = second_opt_in(code, email, datetime.utcnow().isoformat())
    if not result:
        return render(
            request,
            "home/newsletter_confirm_error.html",
            {
                "subscribe_page_url": reverse(newsletter_subscribe),
                "unsubscribe_page_url": reverse(newsletter_unsubscribe),
                "subscriber_email": email,
            },
        )
    return render(
        request,
        "home/newsletter_double_optin_confirm.html",
        {
            "subscribe_page_url": reverse(newsletter_subscribe),
            "unsubscribe_page_url": reverse(newsletter_unsubscribe),
            "subscriber_email": email,
        },
    )


def newsletter_unsubscribe(request, subscriber_email=""):
    if request.method == "POST":
        if "subscriber_email" not in request.POST:
            return HttpResponse(status=400)
        email = request.POST["subscriber_email"]
        unsubscribe(email, datetime.utcnow().isoformat())
        return render(
            request,
            "home/newsletter_unsubscribe_confirm.html",
            {
                "subscribe_page_url": reverse(newsletter_subscribe),
                "unsubscribe_page_url": reverse(newsletter_unsubscribe),
                "subscriber_email": email,
            },
        )
    elif request.method == "GET":
        email = subscriber_email
        if "confirm" in request.GET:
            result = unsubscribe(email, datetime.utcnow().isoformat())
            return render(
                request,
                "home/newsletter_unsubscribe_confirm.html",
                {
                    "subscribe_page_url": reverse(newsletter_subscribe),
                    "unsubscribe_page_url": reverse(newsletter_unsubscribe),
                    "subscriber_email": email,
                },
            )
        return render(
            request,
            "home/newsletter_unsubscribe.html",
            {
                "subscribe_page_url": reverse(newsletter_subscribe),
                "unsubscribe_page_url": reverse(newsletter_unsubscribe),
                "subscriber_email": email,
            },
        )


def newsletter_bounce(request):
    if request.method != "POST":
        return HttpResponse(status=400)
    if "signature" not in request.POST:
        return HttpResponse(status=400)

    return mailgun_handle_bounce(request.POST)
