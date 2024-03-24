from django.contrib import admin

# Register your models here.
from .models import *
from .models import ParentProfile

admin.site.register(Parent)
admin.site.register(Pediatrician)
admin.site.register(Psychologist)
admin.site.register(InformationBoard)
admin.site.register(ExtraInfo)
admin.site.register(Login)
admin.site.register(ParentProfile)
admin.site.register(Feedback)
admin.site.register(Comment)
admin.site.register(WorkshopSummary)
admin.site.register(PsychologistSchedule)

