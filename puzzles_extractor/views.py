# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from puzzles_extractor.models import get_all_puzzles


def list_all_puzzles(request):
    brainzilla_puzzles = get_all_puzzles()
    return render(request,
                  "puzzles.html",
                  {"puzzles": brainzilla_puzzles})

