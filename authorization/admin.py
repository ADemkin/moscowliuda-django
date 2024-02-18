from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from authorization.models import MoscowUser


class MoscowUserAdmin(UserAdmin):
    list_display = ('id', 'firstname', 'surname', 'patronymic', 'email', 'phone', 'telegram', 'instagram')
    fieldsets = (
        (None, {"fields": (
            "firstname", "surname", "patronymic", "password",
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
            'email', 'password1', 'password2', 'firstname', 'surname', 'patronymic', 'phone', 'telegram', 'instagram'),
        }),
    )
    ordering = ('email',)

admin.site.register(MoscowUser, MoscowUserAdmin)
