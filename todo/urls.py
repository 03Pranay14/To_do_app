from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home-page"),
    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('delete-task/<str:name>',views.DeleteTask,name='delete'),
    path('update/<str:name>',views.Update,name='update'),
    path('logout/',views.logoutpage,name='logout'),
    
]
