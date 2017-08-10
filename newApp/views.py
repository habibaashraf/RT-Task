from django.http import HttpResponse
from .models import User
from django.views.generic.edit import CreateView

def index(request):
   return HttpResponse("<h1> Hello </h1>");


def saved(request,id):
   return HttpResponse("<h1> Thanks, Data Saved! </h1>");

class addData(CreateView):
    model=User
    fields=['Name','Email','Phone','Age','Gender','Comment']