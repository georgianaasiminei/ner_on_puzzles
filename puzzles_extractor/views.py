# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from puzzles_extractor.models import get_all_puzzles, get_puzzle
from puzzles_extractor.services import ner_with_spcy, ner_with_flair, flair_for_displacy


def spacy_ner(request, puzzle_id):
    puzzle = get_puzzle(puzzle_id)
    ner_html = ner_with_spcy(puzzle.clues)
    return render(request,
                  "ner_clues.html",
                  {"clues": ner_html})


def flair_ner(request, puzzle_id):
    puzzle = get_puzzle(puzzle_id)
    # flair_sentences = ner_with_flair(puzzle.clues)
    flair_sentences = flair_for_displacy(puzzle.clues)
    return render(request,
                  "flair_clues.html",
                  {"clues": flair_sentences})


def list_all_puzzles(request):
    brainzilla_puzzles = get_all_puzzles()
    return render(request,
                  "puzzles.html",
                  {"puzzles": brainzilla_puzzles}
                  )
