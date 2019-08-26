from django.contrib import admin
from .models import Uye, BaskanMesaji, UyelikBasvurusu, Contact, Kurul, \
        Etkinlik, Proje, Egitim, Haber, Duyuru

class UyeAdmin(admin.ModelAdmin):
    exclude = ('uye_slug',)
admin.site.register(Uye, UyeAdmin)

class BaskaninmesajiAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaskanMesaji, BaskaninmesajiAdmin)

class KurulAdmin(admin.ModelAdmin):
    exclude = ('kurul_slug', 'kurul_name_capital')
    list_display = ('kurul_name', 'kurul_ustkurul')
admin.site.register(Kurul, KurulAdmin)

class EtkinlikAdmin(admin.ModelAdmin):
    exclude = ('etkinlik_slug',)
admin.site.register(Etkinlik, EtkinlikAdmin)

class EgitimAdmin(admin.ModelAdmin):
    exclude = ('egitim_slug',)
admin.site.register(Egitim, EgitimAdmin)

class ProjeAdmin(admin.ModelAdmin):
    exclude = ('proje_slug',)
admin.site.register(Proje, ProjeAdmin)

class HaberAdmin(admin.ModelAdmin):
    exclude = ('haber_slug',)
admin.site.register(Haber, HaberAdmin)

class DuyuruAdmin(admin.ModelAdmin):
    exclude = ('duyuru_slug',)
admin.site.register(Duyuru, DuyuruAdmin)

class UyelikBasvurusuAdmin(admin.ModelAdmin):
    pass
admin.site.register(UyelikBasvurusu, UyelikBasvurusuAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)

admin.site.site_header = 'TÜRKAB Yönetim Paneli'