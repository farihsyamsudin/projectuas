from django.contrib import admin
from django.urls import path, include, re_path
from logbook.views import *
from logbook.viewstides import *
from logbook.viewslogbook import *
from news.views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from logbook.viewset_api import *
from rest_framework import routers
from django.conf import settings
from django.views.static import serve

router = routers.DefaultRouter()
router.register('hasiltangkap', HasilTangkapViewset)
router.register('kapal', KapalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpage/', AdminPage, name='adminpage'),
    path('', index, name='homepage'),
    path('tides/', tidesInfo, name='tides'),
    path('api/docs/', APIDocs, name='APIDocs'),
    path('berita/', BeritaView, name='berita'),
    path('berita/<int:pk>', detailBerita, name='detailberita'),
    path('berita/<str:cat>', beritaCategory, name='kategoriberita'),
    path('berita/tambahberita/', tambahBerita, name='tambahberita'),
    path('berita/editberita/<int:pk>', editBerita, name='editberita'),
    path('berita/hapusberita/<int:pk>', hapusBerita, name='hapusberita'),
    path('data/kapal/', dataKapal, name='datakapal'),
    path('data/kapal/input/', createKapal, name='inputkapal'),
    path('data/kapal/edit/<int:id>/', updateKapal, name='updatekapal'),
    path('data/kapal/delete/<int:id>/', deleteKapal, name='deletekapal'),
    path('data/hasiltangkap/', datalogbook, name='datalogbook'),
    path('data/hasiltangkap/grafik/', grafikHasilTangkap, name='grafikhasiltangkap'),
    path('data/hasiltangkap/input/', crateHasilTangkap, name='inputhasiltangkap'),
    path('data/hasiltangkap/edit/<int:id>/', updateHasilTangkap, name='updatehasiltangkap'),
    path('data/hasiltangkap/delete/<int:id>/', deleteHasilTangkap, name='deletehasiltangkap'),
    path('data/hasiltangkap/export/xls/', export_xls_hasiltangkap, name='exporthasiltangkap'),
    path('data/kapal/export/xls/', export_xls_kapal, name='exportkapal'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('simpanpesan/', SimpanPesan, name='simpanpesan'),
    path('hapuspesan/<int:id>', HapusPesan, name='hapuspesan'),
    path('simpanpeta/', SimpanPeta, name='simpanpeta'),
    path('editpeta/', EditPeta, name='editpeta'),
    path('hapuspeta/<int:id>', HapusPeta, name='hapuspeta'),
    path('unset_session/', unset_session, name='unset_session'),
    path('api/', include(router.urls)),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)