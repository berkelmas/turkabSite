from django.shortcuts import render, redirect
from .models import Uye, BaskanMesaji, UyelikBasvurusu, Contact, \
    Kurul, Etkinlik, Proje, Egitim

from django.core.paginator import Paginator

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
    return render(request, 'mainapp/onurkurulu.html', { 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def kuruldetay(request, kurulslug):
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)

    kurul = Kurul.objects.get(kurul_slug= kurulslug)

    return render(request, 'mainapp/kuruldetay.html', { 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt, 'kurul' : kurul })


def etkinlikler(request):
    etkinlik_list = Etkinlik.objects.all()

    paginator = Paginator(etkinlik_list, 4)
    page = request.GET.get('page')
    etkinlikler = paginator.get_page(page)

    ucetkinlik = Etkinlik.objects.all()[:3]
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/etkinlikler.html', { 'etkinlikler' : etkinlikler, 'ucetkinlik' : ucetkinlik, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def projeler(request):
    proje_list = Proje.objects.all()

    paginator = Paginator(proje_list, 4)
    page = request.GET.get('page')
    projeler = paginator.get_page(page)

    ucproje = Projeler.objects.all()[:3]
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/projeler.html', { 'projeler' : projeler, 'ucproje' : ucproje, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def egitimler(request):
    egitim_list = Egitim.objects.all()

    paginator = Paginator(egitim_list, 4)
    page = request.GET.get('page')
    egitimler = paginator.get_page(page)

    ucegitim = Egitim.objects.all()[:3]
    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/egitimler.html', { 'egitimler' : egitimler, 'ucegitim' : ucegitim, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def egitimdetay(request, egitimslug):
    egitim = Egitim.objects.get(egitim_slug= egitimslug)

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/egitimdetay.html', { 'egitim' : egitim, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def projedetay(request, projeslug):
    proje = Proje.object.get(proje_slug= projeslug)

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/projedetay.html', { 'proje' : proje, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })    

def etkinlikdetay(request, etkinlikslug):
    etkinlik = Etkinlik.objects.get(etkinlik_slug= etkinlikslug)

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(reguest, 'mainapp/etkinlikdetay.html', { 'etkinlik' : etkinlik, 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

def birliksozlesmesi(request):
    return render(request, 'mainapp/birliksozlesmesi.html')

def uyelikbasvurusu(request):

    kurullarUst = Kurul.objects.filter(kurul_ustkurul__isnull = True)
    kurullarAlt = Kurul.objects.filter(kurul_ustkurul__isnull = False)
    return render(request, 'mainapp/uyelikbasvurusu.html', { 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })

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

    return render(request, 'mainapp/iletisim.html', { 'kurullarUst' : kurullarUst, 'kurullarAlt' : kurullarAlt })
