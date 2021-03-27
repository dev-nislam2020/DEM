from django import forms

from expense.models import Category, Expense


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
        labels = {
            'name':'Category Name'
        }
