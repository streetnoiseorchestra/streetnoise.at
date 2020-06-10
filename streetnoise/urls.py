from django.conf import settings
from django.conf.urls import include, url, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from home.views import newsletter_subscribe, newsletter_confirm, newsletter_unsubscribe

admin.site.login = staff_member_required(login_url="/", redirect_field_name="")(
    admin.site.login
)

# from search import views as search_views

urlpatterns = [
    url(r"^django-admin/", admin.site.urls),
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"", include("allauth.urls")),  # Creates urls like yourwebsite.com/login/
    url(r"^accounts/", include("allauth.urls")),
    url(r"^blog/", include("blog.urls", namespace="blog")),
    url(r"^newsletter/subscribe/", newsletter_subscribe, name="Subscribe"),
    url(r"^newsletter/unsubscribe/", newsletter_unsubscribe, name="Unsubscribe"),
    url(r"^newsletter/confirm/", newsletter_confirm, name="Confirm Subscription"),
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
