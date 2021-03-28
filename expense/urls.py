from django.urls import path

from expense.views import (BudgetCreateView, BudgetUpdateView,
                           CategoryCreateView, CategoryUpdateView,
                           ExpenseCreateView, ExpenseDeleteView,
                           ExpensePreviousCreateView, ExpenseUpdateView,
                           MonthView, TodayView, WeekView)

urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('create/previous', ExpensePreviousCreateView.as_view(), name='expense-create-previous'),
    path('category/<int:pk>/create/', ExpenseCreateView.as_view(), name='category-expense-create'),
    path('category/<int:pk>/create/previous', ExpensePreviousCreateView.as_view(), name='category-expense-create-previous'),
    path('<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),

    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),

    path('budget/create/', BudgetCreateView.as_view(), name='budget-create'),
    path('budget/<int:pk>/update/', BudgetUpdateView.as_view(), name='budget-update'),

    path('<int:year>/<str:month>/<int:day>/', TodayView.as_view(), name="archive_day"),
    path('<int:year>/<int:week>/week/', WeekView.as_view(), name="archive_week"),
    path('<int:year>/<str:month>/', MonthView.as_view(), name="archive_month"),
]
