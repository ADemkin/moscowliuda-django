from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User

admin.site.site_header = 'Moscowliuda.ru'


class MoscowUserAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'patronymic', 'email', 'phone', 'telegram', 'instagram')
    fieldsets = (
        (None, {"fields": (
            "first_name", "last_name", "patronymic", "password",
            "email", "phone", "telegram", "instagram"
        )}),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'phone', 'telegram',
                'instagram'),
        }),
    )
    ordering = ('email',)


admin.site.register(User, MoscowUserAdmin)
