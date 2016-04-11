# coding=utf-8
import os
import codecs
import json
import sys, locale
# from aqt.utils import showInfo
# sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

# file = u"/path/to/text.txt"
# # select deck
# did = mw.col.decks.id("ImportDeck")
# mw.col.decks.select(did)
# # set note type for deck
# m = mw.col.models.byName("Basic")
# deck = mw.col.decks.get(did)
# deck['mid'] = m['id']
# mw.col.decks.save(deck)
# # import into the collection
# ti = TextImporter(mw.col, file)

def inReading(idx, character, expression, data):
    print(expression[idx:])
    expression = expression[idx:]
    expression = expression[:expression.index(']')]
    for r in data[character]['reading']:
        print(type(r), r)
        print(type(expression), expression)
        if r in expression:
            return True
    return False


# def injectReadingData(data, expression):
#     n = 0
#     phonetics = []
#     expression = i.split("\t")[0]
#
#     for idx, c in enumerate(expression):
#         if c in data:
#             if inReading(idx, c, expression, data):
#                 if data[c]['raw'] not in phonetics:
#                     raw = data[c]['raw']
#                     delim_index = raw.index('→')
#                     chars = (raw)[delim_index:]
#                     highlight_index = (chars).index(c)
#                     total_index = delim_index + highlight_index
#                     highlighted = raw[:total_index] + '<b>' + c + '</b>' + raw[total_index + 1:]
#                     phonetics.append(highlighted)
#     if phonetics:
#         n = n + 1
#
#     row = i.split("\t")


# def highlight():
#     highlight_index = (chars).index(c)
#     total_index = delim_index + highlight_index
#     highlighted = raw[:total_index] + '<b>' + c + '</b>' + raw[total_index + 1:]

def getPhonetic(expression, data):
    expression = expression.decode('utf-8', 'ignore')
    for idx, c in enumerate(expression):
        # print '燥'.decode('utf8')
        if c in data:
            # print('here', data[c])
            if inReading(idx, c, expression, data):
                print('2here2', data[c])
                raw = data[c]['raw']
                # showInfo(raw)
                print(raw)
                # print('here',raw.decode('utf-8'))


def getHighlightedPhonetics(expression):
    input_file = 'data.json'
    data = getReadingData(input_file)
    # print(data[u'燥'])
    getPhonetic(expression, data)


def getReadingData(input_file):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), input_file)
    file = codecs.open(file_path, 'r', 'utf-8')
    data = json.load(file)
    return data


if __name__ == '__main__':
    # getHighlightedPhonetics('消防[しょう]')
    getHighlightedPhonetics('この 町[まち]には 消防署[しょうぼうしょ]が 1[ひと]つしかありません。')
