from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login"),
    path("logout/", views.log_out,name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
]