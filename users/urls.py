from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/", views.log_out,name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]