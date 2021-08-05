from django.contrib import admin
from .models import UserAccounts
from .forms import UserAccountCreationForm
from django.contrib.auth.admin import UserAdmin

class UserAccountAdmin(UserAdmin):
  model = UserAccounts
  add_form = UserAccountCreationForm

  fieldsets = (
    *UserAdmin.fieldsets,
    (
      'Employee Detail',
      {
        'fields': (
          'accountname',
          'employeeID'
        )
      }
    )
  )
# Register your models here.
admin.site.register(UserAccounts, UserAccountAdmin)