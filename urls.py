from django.contrib import admin
from django.conf.urls import url, include
from  django.contrib.auth import views
from django.contrib.auth.views import auth_login,auth_logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', include('blogapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)