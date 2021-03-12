from typing import List

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


def flair_for_displacy(puzzle_clues: str) -> List:
    sentences = [Sentence(sent, use_tokenizer=True) for sent in split_single(puzzle_clues)]

    tagger = SequenceTagger.load('ner')

    tagger.predict(sentences)

    sentences_dict = [sentence.to_dict(tag_type='ner') for sentence in sentences]

    result = []
    for dict_flair in sentences_dict:
        for idx in dict_flair['entities']:
            idx['end'] = idx.pop('end_pos')
            idx['start'] = idx.pop('start_pos')
            idx['label'] = idx.pop('labels')[0].value
        dict_flair['ents'] = dict_flair.pop('entities')

        result.append(displacy.render(dict_flair, jupyter=False, style='ent', manual=True))

    return result

    # sentence = Sentence(puzzle_clues)
    #
    # tagger = SequenceTagger.load('ner')
    #
    # tagger.predict(sentence)
    #
    # dict_flair = sentence.to_dict(tag_type='ner')

    # for idx in dict_flair['entities']:
    #     idx['end'] = idx.pop('end_pos')
    #     idx['start'] = idx.pop('start_pos')
    #     idx['label'] = idx.pop('labels')[0].value
    # dict_flair['ents'] = dict_flair.pop('entities')
    #
    # return displacy.render(dict_flair, jupyter=False, style='ent', manual=True)
