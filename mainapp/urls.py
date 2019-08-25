from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, about, uyedetail, baskaninmesaji, \
                    uyelikbasvurusu, uyelikbasvurusuformu, iletisim, \
                    yonetim, onurkurulu, kuruldetay, egitimler, projeler, \
                    etkinlikler, birliksozlesmesi, egitimdetay, etkinlikdetay, \
                    projedetay
                    

urlpatterns = [
    path('', index, name="index"),
    path('hakkimizda', about, name="about"),
    path('baskanin-mesaji', baskaninmesaji, name="baskaninmesaji"),
    path('yonetim', yonetim, name="yonetim"),
    path('onur-kurulu', onurkurulu, name="onurkurulu"),
    path('birlik-sozlesmesi', birliksozlesmesi, name="birliksozlesmesi"),
    path('egitimler', egitimler, name="egitimler"),
    path('egitim/<slug:egitimslug>', egitimdetay, name="egitimdetay"),
    path('projeler', projeler, name="projeler"),
    path('proje/<slug:projeslug>', projedetay, name="projedetay"),
    path('yayinlar', etkinlikler, name="etkinlikler"),
    path('yayın/<slug:etkinlikslug>', etkinlikdetay, name="etkinlikdetay"),
    path('kurul/<slug:kurulslug>', kuruldetay, name="kuruldetay"),
    path('uye/<slug:uyeslug>', uyedetail, name="uyedetail"),
    path('uyelik-basvurusu', uyelikbasvurusu, name="uyelikbasvurusu"),
    path('uyelik-basvurusu-formu', uyelikbasvurusuformu, name="uyelikbasvurusuformu"),
    path('iletisim', iletisim, name="iletisim")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
