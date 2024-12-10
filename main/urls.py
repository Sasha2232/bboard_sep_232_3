from .views import index, other_page, BBLoginView, profile
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]
