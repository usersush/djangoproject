from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('login/', views.loginview, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('signup/', views.signupview, name='signup'),
    path('otp/', views.otpview, name='otp'),
    path('profile/', views.profileview, name='profile'),
    path('u_profile/', views.edit_profileview, name='edit_profile')
]

'''
<div class='border border-danger bg-danger text-center mb-3 py-1 alert-dismissible fade show' style="border-radius: 0.8rem;" role="alert">
  <span class='text text-white'>
    {{ message }}
  </span>
</div>
{% else %}
<div class="border border-{{ message.tags }} bg-{{ message.tags }} text-center mb-3 py-1 alert-dismissible fade show" style="border-radius: 0.8rem;" role="alert">
  <span class='text text-white'>
    {{ message }}
  </span>
</div>

'''
