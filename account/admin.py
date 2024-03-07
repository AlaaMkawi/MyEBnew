from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Parent)
admin.site.register(Pediatrician)
admin.site.register(Psychologist)
admin.site.register(InformationBoard)
admin.site.register(ExtraInfo)
admin.site.register(Login)
