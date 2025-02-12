import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView,AccountDeleteView
from projectapp.views import ProjectListView, ProjectDetailView, ProjectCreateView

app_name = "projectapp"

urlpatterns = [

    path('list/', ProjectListView.as_view(), name='list'),

    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
]