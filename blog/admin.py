from django.contrib import admin
from .models import Post

#register your models here

#register this model with admin site
admin.site.register(Post)
