from django.http import HttpResponse
from .models import Collection, Piece
from django.views import  generic
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm



class index(generic.ListView):
    template_name = 'genre/genretemplate.html'
    def get_queryset(self):
        return Collection.objects.all()


class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailtemplate.html'
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'genre/register.html', {'form': form})