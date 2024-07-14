from django.contrib import admin
from .models import * 

admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(Season)
admin.site.register(Episode)