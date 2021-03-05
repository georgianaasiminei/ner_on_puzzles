from django.conf.urls import url

from puzzles_extractor import views

app_name = 'puzzles_extractor'
urlpatterns = [
    url('puzzles/', views.list_all_puzzles, name='list_all_puzzles'),
    url('ner/(?P<puzzle_id>.+?)', views.ner, name='ner'),
]
