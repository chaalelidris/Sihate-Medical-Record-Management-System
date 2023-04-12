from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# ------------------------------------------------------------------------
# ------------------------------Admin urls--------------------------------
# ------------------------------------------------------------------------

urlpatterns = [
    path("admin/", admin.site.urls),
    # -------------------------------------------------------------------
    # ----------------------- Home --------------------------------------
    # -------------------------------------------------------------------
    path("", include("home_page.urls")),
    # -------------------------------------------------------------------
    # ----------------------- Users --------------------------------------
    # -------------------------------------------------------------------
    path("user/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = ""
admin.site.site_title = "Admin"
admin.site.index_title = "Sihate Administration"
