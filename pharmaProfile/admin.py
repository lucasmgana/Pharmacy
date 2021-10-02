from django.contrib import admin
from django.contrib.auth.models import Group

# our models
from pharmaProfile.models import Profile, Expense


admin.site.register([Profile, Expense])
admin.site.unregister(Group)