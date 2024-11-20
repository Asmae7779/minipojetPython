from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = TaskForm()
    

    tasks = task.objects.all()
    context = {'tasks':tasks,'forms': form}
    return render(request, 'tasks/list.html', context)