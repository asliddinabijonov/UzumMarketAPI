from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group
from .models import *


class CastumUserAdmin(UserAdmin):
    fieldsets = [
        ('Auth', {
            'fields': ['username', 'password']
        },
         ),
        ('Details',
         {'fields': ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'birth_date', 'gender',
                     'address', 'date_joined'],
          },
         )
    ]


admin.site.register(User, CastumUserAdmin)
admin.site.unregister(Group)
