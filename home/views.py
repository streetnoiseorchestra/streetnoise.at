from django.http import HttpResponse


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def ajax_newsletter_subscribe(request):
    return HttpResponse(status=410)


def newsletter_subscribe(request):
    return HttpResponse(status=410)


def newsletter_confirm(request):
    return HttpResponse(status=410)


def newsletter_unsubscribe(request, subscriber_email=""):
    return HttpResponse(status=410)


def newsletter_bounce(request):
    return HttpResponse(status=410)
