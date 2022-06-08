from django.shortcuts import render
from .models import server
from .forms import serverForm

def create_server(request):
    context = {}

from = serverForm(request.POST or None)
if form.is_valid():
    form.save()
    return redirect('/')

context ['form'] = form
return render(request, 'create_server.html', context)
# Create your views here.
