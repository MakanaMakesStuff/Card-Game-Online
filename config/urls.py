from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("cms/", include(wagtailadmin_urls)),
    path("", include("apps.war.urls")),
    path("", include("apps.blackjack.urls")),
    path("", include(wagtail_urls)),
]
