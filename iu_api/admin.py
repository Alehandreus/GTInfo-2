from django.contrib import admin
from .models import UserOnlineActivityObject


#class UserOnlineActivityObjectAdmin(admin.ModelAdmin):
#    pass


admin.site.register(UserOnlineActivityObject)