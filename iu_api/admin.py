from django.contrib import admin
from .models import UserOnlineActivityObject, TrackedUserObject


#class UserOnlineActivityObjectAdmin(admin.ModelAdmin):
#    pass


admin.site.register(UserOnlineActivityObject)
admin.site.register(TrackedUserObject)