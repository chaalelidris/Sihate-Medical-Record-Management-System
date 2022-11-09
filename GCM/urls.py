from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('', include('e_sante.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


admin.site.site_header = ''
admin.site.site_title = 'Admin'
admin.site.index_title = 'Sihat_e Administration'
