from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, about, uyedetail, baskaninmesaji, \
                    uyelikbasvurusu, uyelikbasvurusuformu, iletisim

urlpatterns = [
    path('', index, name="index"),
    path('hakkimizda', about, name="about"),
    path('baskanin-mesaji', baskaninmesaji, name="baskaninmesaji"),
    path('uye/<slug:uyeslug>', uyedetail, name="uyedetail"),
    path('uyelik-basvurusu', uyelikbasvurusu, name="uyelikbasvurusu"),
    path('uyelik-basvurusu-formu', uyelikbasvurusuformu, name="uyelikbasvurusuformu"),
    path('iletisim', iletisim, name="iletisim")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
