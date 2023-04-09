from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    data_tombol = range(1, 201) # range angka 1-200
    context = {'tombol': data_tombol}
    return render(request, 'satria/index.html', context)