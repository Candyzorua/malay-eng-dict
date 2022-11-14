import re
import json
example_input = "aku suka kamu!"


def cleanwords(rawWordString: str) -> list[str]:
    noPunctWords = []
    rawWords = rawWordString.split(" ")
    for w in rawWords:
        noPunctString = re.sub(r'[^\w\s]', '', w)
        noPunctWords.append(noPunctString)
    return noPunctWords

assert(cleanwords(example_input)) == ['aku', 'suka', 'kamu']


def findtranslations(rawWordString: str) -> dict:
    malayWords = cleanwords(rawWordString)
    translationsDict = {}
    with open("malay_eng_dict.json", "r") as f:
        malayDict = json.load(f)
        for w in malayWords:
            if w in malayDict:
                translationsDict[w] = malayDict[w]
            else:
                translationsDict[w] = "n/a"
    return translationsDict

assert(findtranslations(example_input)) == {'aku': 'me; I', 'suka': 'like; enjoy', 'kamu': 'you; your'}

