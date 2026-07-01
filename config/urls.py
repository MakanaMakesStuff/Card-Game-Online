
from django.contrib import admin
from django.urls import path, include
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('cms/', include(wagtailadmin_urls)),
    path("", include("apps.war.urls")),
    path("", include(wagtail_urls)),
]
