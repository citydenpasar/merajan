from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import redirect, render, get_object_or_404
from .models import Komentar, Betara
from .forms import KomentarForm

# Create your views here.
def index(request, komentar_id=None):
    betara_list = Betara.objects.all() # sama dengan betara_list = Betara.objects.raw('SELECT * FROM food_item') 
    if request.method == 'POST':
        form = KomentarForm(request.POST)
        if form.is_valid():
            parent_komentar = None
            if komentar_id:
                parent_komentar = get_object_or_404(Komentar, id=komentar_id)
            form.save(parent_komentar)
            return HttpResponseRedirect('/')
    else:
        form = KomentarForm()

    komentar = Komentar.objects.filter(parent__isnull=True)
    context = {'komentar': komentar, 'form': form, 'betara_list': betara_list}
    return render(request, 'satria/index.html', context)

def purnama(request):
    context = {}
    
    return render(request, 'satria/KPK-Purnama.html', context)

def detailbetara(request,betara_id):
    item = Betara.objects.get(pk=betara_id)
    context = {
        'item':item,
    }
    return render(request,'satria/detailbetara.html',context)


