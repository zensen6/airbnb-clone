from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
]