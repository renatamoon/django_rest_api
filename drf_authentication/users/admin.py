# STANDARD IMPORTS
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# PROJECT IMPORTS
from users.models import UserProfile


class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False  # allows to delete the accounts and the users that are related to it
    verbose_name_plural = 'UserProfiles'


# in this you will be able to visualize everything that we see on Django Admin Pannel
class CustomizedUserAdmin (UserAdmin):
    in_lines = (UserProfileInLine, )


admin.site.unregister(User)  # here we are unregistering the standard user Auth model, then we need to register it again
admin.site.register(User, CustomizedUserAdmin)  # responsible to add the customs fields in line on the admin pannel

admin.site.register(UserProfile)
