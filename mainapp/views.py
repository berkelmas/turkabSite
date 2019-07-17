from django.shortcuts import render, redirect
from .models import Uye, BaskanMesaji, UyelikBasvurusu, Contact

# Create your views here.
def index(request):
    uyeler = Uye.objects.all()
    return render(request, 'mainapp/index.html', {'nbar' : 'index', 'uyeler' : uyeler})

def about(request):
    uyeler = Uye.objects.all()
    return render(request, 'mainapp/about.html', {'nbar' : 'about', 'uyeler' : uyeler})

def uyedetail(request, uyeslug):
    uye = Uye.objects.filter(uye_slug = uyeslug)
    uye = uye[0]
    uyeler = Uye.objects.all()
    return render(request, 'mainapp/uyedetail.html', { 'uye' : uye, 'uyeler' : uyeler})

def baskaninmesaji(request):
    uyeler = Uye.objects.all()
    baskanmesaji = BaskanMesaji.objects.all()[0]
    return render(request, 'mainapp/baskaninmesaji.html', { 'uyeler' : uyeler, 'baskanmesaji' : baskanmesaji })

def uyelikbasvurusu(request):
    uyeler = Uye.objects.all()
    return render(request, 'mainapp/uyelikbasvurusu.html', { 'uyeler' : uyeler })

def uyelikbasvurusuformu(request):
    uyeler = Uye.objects.all()

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
    return render(request, 'mainapp/uyelikbasvurusuformu.html', { 'uyeler' : uyeler })

def iletisim(request):
    uyeler = Uye.objects.all()

    if request.method == 'POST':
        adsoyad = request.POST.get('adsoyad')
        iletisimbilgisi = request.POST.get('iletisimbilgisi')
        mesaj = request.POST.get('mesaj')

        newContact = Contact(iletisim_name= adsoyad, iletisim_contactinfo= iletisimbilgisi, iletisim_mesaj= mesaj)
        newContact.save()
        return redirect('index')

    return render(request, 'mainapp/iletisim.html', { 'uyeler' : uyeler })
