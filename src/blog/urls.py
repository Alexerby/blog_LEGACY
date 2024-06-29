from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('thealternativepath/', admin.site.urls),
    path('blog/', include('articles.urls')),
    path('about/', include('about.urls')),
    path('', include('core.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

