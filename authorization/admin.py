from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from authorization.models import MoscowUser


# Форма для создания пользователя
class MoscowUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MoscowUser
        fields = ('email', 'phone')

    def __init__(self, *args, **kwargs):
        super(MoscowUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['phone'].required = True


# Класс администратора пользователей
class MoscowUserAdmin(UserAdmin):
    add_form = MoscowUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )
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


admin.site.register(MoscowUser, MoscowUserAdmin)
