from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('thealternativepath/', admin.site.urls),
    path('blog/', include('articles.urls')),
    path('about/', include('about.urls')),
    path('', include('core.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

