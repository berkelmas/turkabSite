from django.shortcuts import render, redirect
from .models import Uye, BaskanMesaji, UyelikBasvurusu, Contact, \
    Kurul

# Create your views here.
def index(request):

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/index.html', {'nbar' : 'index', 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt})

def about(request):

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/about.html', {'nbar' : 'about', 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt})

def uyedetail(request, uyeslug):
    uye = Uye.objects.filter(uye_slug = uyeslug)
    uye = uye[0]

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/uyedetail.html', { 'uye' : uye, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt})

def baskaninmesaji(request):

    baskanmesaji = BaskanMesaji.objects.all()[0]

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/baskaninmesaji.html', {'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt, 'baskanmesaji' : baskanmesaji })

def yonetim(request):
    ykUyeler = Uye.objects.filter(uye_yk_durum= True)
    normalUyeler = Uye.objects.filter(uye_yk_durum= False)

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/yonetim.html', {'ykUyeler' : ykUyeler, 'normalUyeler' : normalUyeler, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt})

def onurkurulu(request):
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/onurkurulu.html', { 'kurullarUst' : KurullarUst, 'kurullarAlt' : kurullarAlt })

def uyelikbasvurusu(request):

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/uyelikbasvurusu.html', { 'kurullarUst' : KurullarUst, 'kurullarAlt' : kurullarAlt })

def uyelikbasvurusuformu(request):
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)

    if request.method == 'POST':
        adsoyad = request.POST.get('adsoyad')
        dogumyerivetarihi = request.POST.get('dogumyerivetarihi')
        tckimlikno = request.POST.get('tckimlikno')
        kurum = request.POST.get('kurum')
        uzmanlik = request.POST.get('uzmanlik')
        meslekiunvan = request.POST.get('meslekiunvan')
        telefonnumarasi = request.POST.get('telefonnumarasi')

        newUyelikBasvurusu = UyelikBasvurusu(basvuru_name = adsoyad, basvuru_dogumyeri_tarihi = dogumyerivetarihi, basvuru_tcno = tckimlikno, basvuru_kurum = kurum, basvuru_uzmanlik = uzmanlik, basvuru_meslekiunvan = meslekiunvan, basvuru_telefon = telefonnumarasi)
        newUyelikBasvurusu.save()
        return redirect('index')
    return render(request, 'mainapp/uyelikbasvurusuformu.html', { 'kurullarUst' : KurullarUst, 'kurullarAlt' : kurullarAlt })

def iletisim(request):
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)

    if request.method == 'POST':
        adsoyad = request.POST.get('adsoyad')
        iletisimbilgisi = request.POST.get('iletisimbilgisi')
        mesaj = request.POST.get('mesaj')

        newContact = Contact(iletisim_name= adsoyad, iletisim_contactinfo= iletisimbilgisi, iletisim_mesaj= mesaj)
        newContact.save()
        return redirect('index')

    return render(request, 'mainapp/iletisim.html', { 'kurullarUst' : KurullarUst, 'kurullarAlt' : kurullarAlt })
