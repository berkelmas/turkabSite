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
