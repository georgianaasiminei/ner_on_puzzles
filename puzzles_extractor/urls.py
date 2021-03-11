from django.conf.urls import url

from puzzles_extractor import views

app_name = 'puzzles_extractor'
urlpatterns = [
    url('puzzles/', views.list_all_puzzles, name='list_all_puzzles'),
    url('spacy/(?P<puzzle_id>.+?)', views.spacy_ner, name='spacy'),
    url('flair/(?P<puzzle_id>.+?)', views.flair_ner, name='flair'),
]
