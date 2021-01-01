from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('aa', views.profile,name='profile'),
    path('bb', views.register,name='register'),
    path('cc', views.password,name='password'),
    path('dd', views.signup,name='signup'),
    path('project', views.project,name='project'),
    path('login', views.login,name='login'),

]