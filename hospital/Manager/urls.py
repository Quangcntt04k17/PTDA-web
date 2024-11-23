from django.urls import path
from . import views
from .views import get_csrf_token
from .views import GetAccountsView 


urlpatterns = [
    path('profile/', views.ManagerProfileView.as_view(), name='Manager-profile'),
    path('register', views.CreateManagerView.as_view(), name='create_Manager'),
    path('update/', views.UpdateManagerView.as_view(), name='update_Manager'),
    path('login/', views.LoginView.as_view(), name='login_Manager'),
    path('get_csrf/', get_csrf_token),
    path('accounts/', GetAccountsView.as_view(), name='admin_list'),
]

