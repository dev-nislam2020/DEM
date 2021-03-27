from datetime import date, timedelta

from django.core.paginator import Paginator
from django.db.models import Count, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.dates import (DayArchiveView, MonthArchiveView,
                                        WeekArchiveView)
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from expense.forms import CategoryForm, ExpenseForm, ExpensePreviousForm
from expense.models import Category, Expense


# Create your views here.
def report(expense_list):
    data = {}
    amount = expense_list.all().aggregate(Sum('amount'))['amount__sum']
    if amount is None:
        data['total_amount'] = 0
    else:
        data['total_amount'] = expense_list.all().aggregate(Sum('amount'))['amount__sum']
    data['trax'] = expense_list.count()
    data['category_count'] = expense_list.values_list('category', flat=True).distinct().count()
    return data

def get_day_expense(obj, today):
    expense_list = obj.filter(create_at__day=today.day)
    return report(expense_list)

def get_week_expense(obj, today):
    current_week = today.isocalendar()[1]
    expense_list = obj.filter(create_at__week=current_week)
    return report(expense_list)

def get_month_expense(obj, today):
    expense_list = obj.filter(create_at__month=today.month)
    return report(expense_list)
    

class HomeView(TemplateView):
    template_name = 'expense/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)

        expense = Expense.objects.all()
        today = date.today()
        current_week = today.isocalendar()[1]

        data = {}
        data['day'] = get_day_expense(expense, today)
        data['week'] = get_week_expense(expense, today)
        data['month'] = get_month_expense(expense, today)

        context['today'] = today
        context['reports'] = data
        return context

class ExpenseCreateView(CreateView):
    form_class = ExpenseForm
    template_name = 'expense/create.html'
    success_url = reverse_lazy('expense-create')
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExpenseCreateView, self).get_context_data(**kwargs)
        expense_list = Expense.objects.all()
        paginator = Paginator(expense_list, 9)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Add in a QuerySet of all the books
        context['page_obj'] = page_obj
        context['page_name'] = "Add Expense"
        context['is_previose'] = True
        return context
    
    def form_valid(self, form):
        form.instance.create_at = date.today()
        return super(ExpenseCreateView, self).form_valid(form)


class ExpensePreviousCreateView(CreateView):
    form_class = ExpensePreviousForm
    template_name = 'expense/create.html'
    success_url = reverse_lazy('expense-create')
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExpensePreviousCreateView, self).get_context_data(**kwargs)
        expense_list = Expense.objects.all()
        paginator = Paginator(expense_list, 9)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Add in a QuerySet of all the books
        context['page_obj'] = page_obj
        context['page_name'] = "Add Previouse Expense"
        
        return context


class ExpenseUpdateView(UpdateView):
    form_class = ExpenseForm
    template_name = 'expense/update.html'
    success_url = reverse_lazy('expense-create')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExpenseUpdateView, self).get_context_data(**kwargs)
        expense_list = Expense.objects.all()
        paginator = Paginator(expense_list, 9)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Add in a QuerySet of all the books
        context['page_obj'] = page_obj
        return context
    
    def get_queryset(self):
        return Expense.objects.all()
    
class ExpenseDeleteView(DeleteView):
    form_class = ExpenseForm
    template_name = 'expense/delete.html'
    success_url = reverse_lazy('expense-create')
    
    def get_queryset(self):
        return Expense.objects.all()

class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'expense/category/list.html'
    success_url = reverse_lazy('category-create')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['category_list'] = Category.objects.all()
        return context

class CategoryUpdateView(UpdateView):
    form_class = CategoryForm
    template_name = 'expense/category/update.html'
    success_url = reverse_lazy('category-create')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['category_list'] = Category.objects.all()
        category = Category.objects.all()
        for cat in category:
            print(cat.expense_set.all())
        return context

    def get_queryset(self):
        return Category.objects.all()
    
class TodayView(DayArchiveView):
    queryset = Expense.objects.all()
    date_field = "create_at"
    allow_future = True
    template_name = 'expense/report/day.html'

class WeekView(WeekArchiveView):
    queryset = Expense.objects.all()
    date_field = "create_at"
    template_name = 'expense/report/week.html'
    week_format = "%W"
    allow_future = True

class MonthView(MonthArchiveView):
    queryset = Expense.objects.all()
    date_field = "create_at"
    template_name = 'expense/report/month.html'
    allow_future = True
