from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("home_page.urls")),
    path("", include("e_sante.urls")),
    path("", include("medicalfile.urls")),
    path("", include("medical_office.urls")),
    path("", include("doctor.urls")),
    path("", include("patient.urls")),
    path("", include("appointment.urls")),
    path("", include("prescription.urls")),
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]


admin.site.site_header = ""
admin.site.site_title = "Admin"
admin.site.index_title = "Sihat_e Administration"
