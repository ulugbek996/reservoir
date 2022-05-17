from django.contrib import admin
from .models import Reservoir,Target,Indicator,History

admin.site.register(Reservoir)
admin.site.register(Target)
admin.site.register(Indicator)
admin.site.register(History)
