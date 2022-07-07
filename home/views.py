from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.templatetags.static import static

from .newsletter import first_opt_in, second_opt_in, mailgun_unsubscribe


def handle_newsletter_subscribe(form, host):
    name = form.cleaned_data["subscriber_name"]
    email = form.cleaned_data["subscriber_email"]
    consented_at = datetime.utcnow().isoformat()
    consented_from = "NewsLetterSubscribeForm"
    confirm_url = "https://{}{}".format(host, reverse(newsletter_confirm))
    withdraw_url = "https://{}{}".format(host, reverse(newsletter_unsubscribe))
    return first_opt_in(
        name, email, consented_at, consented_from, confirm_url, withdraw_url
    )


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
        if request.is_ajax:
            return ajax_newsletter_subscribe(request)
        else:
            return HttpResponse(status=400)
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
        return HttpResponse(status=500)
    return render(
        request,
        "home/newsletter_double_optin_confirm.html",
        {
            "subscribe_page_url": reverse(newsletter_subscribe),
            "unsubscribe_page_url": reverse(newsletter_unsubscribe),
            "subscriber_email": email,
        },
    )


def newsletter_unsubscribe(request):
    if request.method == "POST":
        if "subscriber_email" not in request.POST:
            return HttpResponse(status=400)
        email = request.POST["subscriber_email"]
        result = True
        # result = mailgun_unsubscribe(email, datetime.utcnow().isoformat())
        if result == 400:
            return HttpResponse(status=400)
        elif not result:
            return HttpResponse(status=500)
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
        email = None
        if "subscriber_email" in request.GET:
            email = request.GET["subscriber_email"]
        if "confirm" in request.GET:
            result = mailgun_unsubscribe(email, datetime.utcnow().isoformat())
            if result == 400:
                return HttpResponse(status=400)
            elif not result:
                return HttpResponse(status=500)
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