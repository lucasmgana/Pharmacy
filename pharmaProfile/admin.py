from django.contrib import admin
from django.contrib.auth.models import Group

# our models
from pharmaProfile.models import Profile, ProfilePerm, Expense, PharmPermission


admin.site.register([Profile, ProfilePerm, Expense, PharmPermission])
admin.site.unregister(Group)