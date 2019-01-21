from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/choose_digit', views.choose_digit, name='choose_digit'),
    path('<int:question_id>/post_digits', views.post_digits, name='post_digits'),
    path('<int:question_id>/<int:receipt_id>', views.details, name='details'),
    path('<int:question_id>/cast_vote/<int:receipt_id>', views.cast_vote, name='cast_vote'),
    path('list', views.list, name='list'),
    path('receipt', views.receipt, name='receipt'),
    path('<int:receipt_id>/receipt_details', views.receipt_details, name='receipt_details'),
    path('<int:question_id>/count_votes', views.count_votes, name='count_votes'),
    path('<int:question_id>/results', views.results, name='results')
]