from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/choose_digit', views.choose_digit, name='choose_digit'),
    path('<int:question_id>/', views.details, name='details'),
    path('list', views.list, name='list'),
    path('receipt', views.receipt, name='receipt'),
]