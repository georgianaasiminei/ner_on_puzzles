
import en_core_web_sm
from spacy import displacy

nlp = en_core_web_sm.load()


def ner_with_spcy(puzzle_clues: str):
    processed_puzzle = nlp(puzzle_clues)
    return displacy.render(processed_puzzle, jupyter=False, style='ent')
