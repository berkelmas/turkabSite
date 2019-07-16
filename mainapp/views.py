from django.shortcuts import render
from .models import Uye, BaskanMesaji

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
