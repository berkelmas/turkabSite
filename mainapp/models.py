from django.db import models
from ckeditor.fields import RichTextField

from django.template.defaultfilters import slugify
from unidecode import unidecode

# Create your models here.
class Uye(models.Model):
    uye_name = models.CharField(('Üye Adı'), max_length=150)
    uye_kidem = models.CharField(('Üye Kıdemi'), max_length= 150)
    uye_bio = RichTextField(('Üye Biografisi'))
    uye_slug = models.SlugField(unique= True)
    uye_resim = models.ImageField(('Üye Resmi 300x300px'), null= True)

    class Meta:
        verbose_name= 'Üye'
        verbose_name_plural= 'Üyeler'

    def __str__(self):
        return self.uye_name;

    def save(self, *args, **kwargs):
        self.uye_slug = slugify(unidecode(self.uye_name))
        super(Uye, self).save(*args, **kwargs)

class BaskanMesaji(models.Model):
    baskan_mesaji = RichTextField(('Başkanın Mesajı'))

    def __str__(self):
        return 'Başkanın Mesajı'

    class Meta:
        verbose_name = 'Başkanın Mesajı'
        verbose_name_plural = 'Başkanın Mesajı'

class UyelikBasvurusu(models.Model):
    basvuru_name = models.CharField(('Başvurucu İsmi'), max_length= 150)
    basvuru_dogumyeri_tarihi = models.CharField(('Başvurucu Doğum Yeri ve Tarihi'), max_length= 150)
    basvuru_tcno = models.CharField(('Başvurucu TC Numarası'), max_length= 150)
    basvuru_kurum = models.CharField(('Başvurucu Çalıştığı Kurum'), max_length= 150)
    basvuru_uzmanlik = models.CharField(('Başvurucu Uzmanlık Alanı'), max_length= 150)
    basvuru_meslekiunvan = models.CharField(('Başvurucu Mesleki Ünvanı'), max_length= 150)
    basvuru_telefon = models.CharField(('Başvurucu Telefon Numarası'),max_length= 150)

    basvuru_tarihi = models.DateField(('Başvurunun Yapıldığı Tarih'), auto_now_add= True)

    class Meta:
        verbose_name = 'Üyelik Başvurusu'
        verbose_name_plural = 'Üyelik Başvuruları'
        ordering = ('-basvuru_tarihi',)

    def __str__(self):
        return self.basvuru_name

class Contact(models.Model):
    iletisim_name = models.CharField(('Ad-Soyad'), max_length = 150)
    iletisim_contactinfo = models.CharField(('İletişim Adresi'), max_length= 150)
    iletisim_mesaj = models.TextField(('İletişim Mesajı'))

    iletisim_tarihi = models.DateField(('İletişim Tarihi'), auto_now_add= True)

    class Meta:
        verbose_name = 'İletişim Talebi'
        verbose_name_plural = 'İletişim Talepleri'
        ordering = ('iletisim_tarihi',)

    def __str__(self):
        return self.iletisim_name
        
