from datetime import timezone

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['create_at']
    
    def __str__(self):
        return self.name
    
class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    create_at = models.DateField()
    update_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-create_at']
    
    def __str__(self):
        return str(self.amount)

class Budget(models.Model):
    BUDGET_TIME = (
        ('1','DAY'),
        ('1','WEEK'),
        ('1','MONTH'),
    )
    name = models.CharField(max_length=50, unique=True)
    amount = models.IntegerField()
    budget_for = models.CharField(max_length=50, choices=BUDGET_TIME)
    deadline = models.DateField()
    notes = models.TextField(blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
