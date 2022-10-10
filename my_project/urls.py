from django.contrib import admin
from django.urls import path, include

#이미지를 위해 추가한 코드
#from main.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
]

#이미지를 위해 추가한 코드2
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)