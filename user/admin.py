from django import forms
from django.contrib import admin

from user.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("user_name", "password", "first_name", "last_name", "department", "is_admin")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

    list_display = ('first_name', 'last_name', 'user_name', 'department', 'password', 'is_admin')
    list_filter = ('department',)
    search_fields = ('department',)