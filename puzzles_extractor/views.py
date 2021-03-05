# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from puzzles_extractor.models import get_all_puzzles, get_puzzle
from puzzles_extractor.services import ner_with_spcy


def ner(request, puzzle_id):
    puzzle = get_puzzle(puzzle_id)
    ner_html = ner_with_spcy(puzzle.clues)
    return render(request,
                  "ner_clues.html",
                  {"clues": ner_html})


def list_all_puzzles(request):
    brainzilla_puzzles = get_all_puzzles()
    return render(request,
                  "puzzles.html",
                  {"puzzles": brainzilla_puzzles}
                  )
