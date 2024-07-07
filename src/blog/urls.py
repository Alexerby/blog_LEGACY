from django.urls import path, include
from user.admin import admin_site

from django.contrib import admin

urlpatterns = [
    path('thealternativepath/', admin_site.urls),
    path('blog/', include('articles.urls')),
    path('about/', include('about.urls')),
    path('boating/', include('boating.urls')),
    path('', include('core.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

