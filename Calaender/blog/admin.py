from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Schedule

admin.site.register(Post)
admin.site.register(Schedule)