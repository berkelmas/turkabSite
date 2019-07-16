from django.contrib import admin
from .models import Uye, BaskanMesaji

class UyeAdmin(admin.ModelAdmin):
    exclude = ('uye_slug',)
admin.site.register(Uye, UyeAdmin)

class BaskaninmesajiAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaskanMesaji, BaskaninmesajiAdmin)
