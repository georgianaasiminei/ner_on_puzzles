# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from typing import List

from django.db import models


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=160)
    domain = models.CharField(max_length=160)
    puzzles_path = models.CharField(max_length=160)

    def __str__(self):
        return f"Source: {self.name}"


class Puzzle(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    clues = models.TextField()
    url = models.URLField(blank=True)
    source = models.ForeignKey(Source,
                               to_field="id",
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"Puzzle: {self.title}, Clues: {self.clues}"


def get_puzzle(uid: int) -> Puzzle:
    """Return the clues for a given Puzzle ID"""
    result = Puzzle.objects.filter(id=uid)
    if not result:
        raise Exception(f"There is no puzzle with ID {uid}")
    return result.clues


def get_all_puzzles() -> List[Puzzle]:
    return Puzzle.objects.all()
