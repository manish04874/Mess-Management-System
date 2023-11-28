from django.contrib import admin

# Register your models here.
from .models import Category, Attendance, meal, Feedback, MealTicket
admin.site.register(Category)
admin.site.register(Attendance)
admin.site.register(meal)
admin.site.register(Feedback)
admin.site.register(MealTicket)
