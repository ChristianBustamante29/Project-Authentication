from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name="lista_tareas"),
    path('agregar/', views.agregar_tarea, name="agregar_tarea"),
    path('eliminar/<int:task_id>/', views.eliminar_tarea, name="eliminar_tarea"),
    path('register/', views.RegisterView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('forgot-password/', views.ForgotPassword, name="forgot-password"),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name="password-reset-sent"),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name="reset-password"),
]
