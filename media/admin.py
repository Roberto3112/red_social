from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(post)
admin.site.register(comment)
admin.site.register(like)