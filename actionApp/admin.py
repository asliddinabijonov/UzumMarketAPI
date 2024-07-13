from django.contrib import admin
from .models import *

admin.site.register([Banner, Rate, Comment, Favorite])
