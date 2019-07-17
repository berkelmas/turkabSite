from django.contrib import admin
from .models import Uye, BaskanMesaji, UyelikBasvurusu, Contact

class UyeAdmin(admin.ModelAdmin):
    exclude = ('uye_slug',)
admin.site.register(Uye, UyeAdmin)

class BaskaninmesajiAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaskanMesaji, BaskaninmesajiAdmin)

class UyelikBasvurusuAdmin(admin.ModelAdmin):
    pass
admin.site.register(UyelikBasvurusu, UyelikBasvurusuAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
