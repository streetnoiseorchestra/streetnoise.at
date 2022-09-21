from django.conf import settings
from django.urls import include, re_path, path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from birdsong import urls as birdsong_urls

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from home.views import (
    newsletter_subscribe,
    newsletter_confirm,
    newsletter_unsubscribe,
    newsletter_bounce,
)

admin.site.login = staff_member_required(login_url="/", redirect_field_name="")(
    admin.site.login
)

# from search import views as search_views

urlpatterns = [
    re_path(r"^django-admin/", admin.site.urls),
    re_path(r"^admin/", include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"", include("allauth.urls")),  # Creates urls like yourwebsite.com/login/
    re_path(r"^accounts/", include("allauth.urls")),
    re_path(r"^blog/", include("blog.urls", namespace="blog"), name="blog"),
    re_path(r"^newsletter/subscribe/", newsletter_subscribe, name="Subscribe"),
    path(
        "newsletter/unsubscribe/<str:subscriber_email>",
        newsletter_unsubscribe,
        name="newsletter_unsubscribe_email",
    ),
    re_path(
        r"^newsletter/unsubscribe/$",
        newsletter_unsubscribe,
        name="newsletter_unsubscribe",
    ),
    re_path(r"^newsletter/confirm/", newsletter_confirm, name="Confirm Subscription"),
    re_path(r"^newsletter/mailgun", newsletter_bounce, name="Mailgun webhooks"),
    re_path(r"^newsletters/", include(birdsong_urls))
    # url(r'^search/$', search_views.search, name='search'),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    # url(r'', include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    re_path(r"", include(wagtail_urls)),
    prefix_default_language=False,
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
