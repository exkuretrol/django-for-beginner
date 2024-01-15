from django.urls import path, include
from .views import HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("__reload__/", include("django_browser_reload.urls"))
]
