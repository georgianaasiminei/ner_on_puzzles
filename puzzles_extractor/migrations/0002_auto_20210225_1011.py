# Generated by Django 3.1.7 on 2021-02-25 10:11

from django.db import migrations

from puzzles_extractor.extractors import BrainzillaExtractor
from puzzles_extractor.models import Source


def add_brainzilla_puzzles(apps, schema_editor):
    extractor = BrainzillaExtractor()
    puzzles = extractor.extract_all_puzzles()
    # Add Source
    brainzilla_source = Source(
        name="Brainzilla",
        domain="https://www.brainzilla.com",
        puzzles_path="/logic/zebra/"
    )
    brainzilla_source.save()

    # Add puzzles
    for puzzle in puzzles:
        puzzle.save()


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles_extractor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_brainzilla_puzzles)
    ]