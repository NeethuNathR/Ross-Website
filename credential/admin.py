from django.contrib import admin

# Register your models here.
from credential.models import StaffRegistration, staffLogin,Contact

admin.site.register(StaffRegistration)
admin.site.register(staffLogin)
admin.site.register(Contact)
