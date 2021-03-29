from django import forms

from expense.models import Budget, Category, Expense


# Create your forms here.
class ExpenseForm(forms.ModelForm):
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 6, 'cols': 22}))
    class Meta:
        model = Expense
        fields = ['amount', 'notes']

class ExpensePreviousForm(forms.ModelForm):
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 6, 'cols': 22}))
    class Meta:
        model = Expense
        fields = ['amount', 'notes', 'create_at']
        widgets = {
            'create_at': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'amount', 'budget_for', 'notes']
        
