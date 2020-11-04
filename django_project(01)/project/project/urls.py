
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from app.views import contact_download

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('contact-download',contact_download,name='contact_download'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)