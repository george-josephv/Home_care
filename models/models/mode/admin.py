from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Service)

# Register your models here.
