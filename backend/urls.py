from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from backend.settings import MEDIA_URL, MEDIA_ROOT, DEBUG

from app.views import home, eventos

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    path("eventos", eventos.view, name='home'),
    path("", home.view, name='home'),
    
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)