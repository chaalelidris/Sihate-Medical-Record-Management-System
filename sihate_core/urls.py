from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("", include("home_page.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = ""
admin.site.site_title = "Sihate | admin"
admin.site.index_title = "Sihate Administration"
