from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Year, Week, Workout


admin.site.register(User, UserAdmin)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    pass


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    pass


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass

