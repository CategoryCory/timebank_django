from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('is_active', )
    list_per_page = 25
    fieldsets = (
        ('Account Information', {'fields': ('username', 'email', 'first_name', 'last_name', )}),
        ('Contact Information', {'fields': ('street_address', 'street_address_2', 'city', 'state', 'zip_code',
                                            'phone', )}),
        ('Personal and Social Information', {'fields': ('birthday', 'biography', 'facebook', 'twitter', 'instagram',
                                                        'linkedin', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        ('Account Login Information', {'fields': ('last_login', 'date_joined', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)