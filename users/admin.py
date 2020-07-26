from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )




    '''
    what UserAdmin.fieldsets contains:

((None, {'fields': ('username', 'password')}), 
('Personal info', {'fields': ('first_name', 'last_name', 'email')}), 

('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 
'user_permissions')}), 

('Important dates', {'fields': ('last_login', 'date_joined')}))

    '''
    

