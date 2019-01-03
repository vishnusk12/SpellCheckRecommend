'''
Created on 21-Dec-2018

@author: Vishnu
'''

from spellchecker import SpellChecker
import string

exclude = set(string.punctuation)

spell = SpellChecker()

def Spell(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch not in exclude)
    text = ''.join([i for i in text if not i.isdigit()])
    misspelled = spell.unknown(text.split())
    list_word = []
    for word in misspelled:
        dict_word = {}
        dict_word['word'] = word
        dict_word['corrected'] = spell.correction(word)
        dict_word['recommendations'] = list(spell.candidates(word))
        list_word.append(dict_word)
    if len(list_word) > 0:
        list_word = list_word
    else:
        list_word = "No Corrections"
    result = {}
    result['result'] = list_word
    result['success'] = True
    return result
