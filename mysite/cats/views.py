from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat,Breed

# Create your views here.
class CatView(LoginRequiredMixin,View):
    def get(self,request):
        breed_count=Breed.objects.all().count()
        cats_list=Cat.objects.all()

        context={'breed_count':breed_count,'cat_list':cats_list}
        return render(request,'cats/cats_list.html',context)

class CatCreate(LoginRequiredMixin,CreateView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')

class CatDelete(LoginRequiredMixin,DeleteView):
    model=Cat
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')



class BreedView(LoginRequiredMixin,View):
    def get(self,request):
        bl=Breed.objects.all()
        ctx={'breed_list':bl}
        return render(request,'cats/breed_list.html',ctx)

class BreedCreate(LoginRequiredMixin,CreateView):
    model=Breed
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')

class BreedUpdate(LoginRequiredMixin,UpdateView):
    model=Breed
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')

class BreedDelete(LoginRequiredMixin,DeleteView):
    model=Breed
    fields='__all__'
    success_url=reverse_lazy('cats:cat_list')

