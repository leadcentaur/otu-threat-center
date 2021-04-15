
from django.contrib import admin
from django.urls import path, include, re_path
from users.views import profile, login, logout, ProfileDetailView
from main.views import TargetCreateView
from vpn.views import vpn
from inbox.views import inbox, messages
from django.conf import settings
from django.conf.urls.static import static
from importlib import import_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('overview/', include('main.urls')),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('targets/', TargetCreateView.as_view(), name='targets'),
    path('', include('social.apps.django_app.urls'), name='social'),
    path('vpn/', vpn, name='vpn'),
    path('inbox/', inbox, name='inbox'),
    path('inbox/<int:reportnumber>', inbox, name='inbox'),
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
