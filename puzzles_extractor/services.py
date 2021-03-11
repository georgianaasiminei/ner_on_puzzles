import en_core_web_sm

from flair.data import Sentence
from flair.models import SequenceTagger
from segtok.segmenter import split_single
from spacy import displacy

nlp = en_core_web_sm.load()


def ner_with_spcy(puzzle_clues: str):
    processed_puzzle = nlp(puzzle_clues)
    return displacy.render(processed_puzzle, jupyter=False, style='ent')


def ner_with_flair(puzzle_clues: str):
    sentences = [Sentence(sent, use_tokenizer=True) for sent in split_single(puzzle_clues)]

    # load the NER tagger
    tagger: SequenceTagger = SequenceTagger.load('ner')

    # run NER over sentence
    tagger.predict(sentences)

    # iterate over entities and print
    # entities = []
    # for entity in sentences.get_spans('ner'):
    #     print(entity)
    #     entities.append(entity)

    result = []
    for i in sentences:
        result.append(i.to_tagged_string())

    return result
