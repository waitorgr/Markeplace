from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-page/', staff_member_required(views.admin_page), name='admin_page'),
    path('users/', views.user_list, name='user_list'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('profile/', views.view_profile, name='view_profile'),
]