from django.contrib import admin
from blog.models import *

class BlogAdmin(admin.ModelAdmin):
  list_display = ('user','title','content')

admin.site.register(Blog,BlogAdmin)
