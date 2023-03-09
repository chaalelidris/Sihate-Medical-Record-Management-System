from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# ------------------------------------------------------------------------
# ------------------------------Admin urls--------------------------------
# ------------------------------------------------------------------------

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home_page.urls")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
] """


admin.site.site_header = ""
admin.site.site_title = "Admin"
admin.site.index_title = "Sihate Administration"
