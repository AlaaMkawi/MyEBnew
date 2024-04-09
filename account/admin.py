from django.contrib import admin

# Register your models here.
from .models import *
from .models import PediatricianInfoBoard
from .models import Paropinion
from .models import Profile

admin.site.register(Parent)
admin.site.register(Pediatrician)
admin.site.register(Psychologist)
admin.site.register(InformationBoard)
admin.site.register(ExtraInfo)
admin.site.register(Login)
admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(WorkshopSummary)
admin.site.register(PsychologistSchedule)
admin.site.register(Traking)
admin.site.register(Track)

admin.site.register(PediatricianInfoBoard)
admin.site.register(Paropinion)

admin.site.register(Workshop)
admin.site.register(Meeting)
admin.site.register(Profile)




