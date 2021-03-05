from django.conf.urls import url

from puzzles_extractor import views

app_name = 'puzzles_extractor'
urlpatterns = [
    url('', views.list_all_puzzles, name='list_all_puzzles'),
]
