from django.contrib import admin

from expense.models import Category, Expense

# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
