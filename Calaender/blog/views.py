from django.shortcuts import render
from .models import Post
from .models import Schedule

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    schedule = Schedule.objects.all().order_by('-id')
    return render(request, 'index.html', {'schedule_show' : schedule})