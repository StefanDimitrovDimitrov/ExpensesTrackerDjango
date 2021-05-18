from django.urls import path

from app.views.expenses import create_expenses, edit_expenses, delete_expenses
from app.views.index import index
from app.views.profiles import profile_index, edit_profile, delete_profile, create_profile

urlpatterns = (
    # Index
    path('',index, name= 'index'),
    # Expenses
    path('create/', create_expenses, name='create expense'),
    path('edit/', edit_expenses, name='edit expense'),
    path('delete/', delete_expenses, name='delete expense'),
    # Profiles
    path('profile/', profile_index, name='profile index'),
    path('profile/create', create_profile, name='profile index'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/delete', delete_profile, name='delete profile'),
)