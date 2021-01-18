from django.urls import path
# from .views import PostList, PostDetail
from . import views

urlpatterns = [
    path('<int:pk>/',views.update_detail),
    path('', views.enter_detail),
]