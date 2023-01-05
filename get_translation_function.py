import re
import json

#for unit testing
example_input = "Aku Suka Suka"

def cleanwords(rawWordString: str) -> list[str]:
    noPunctWords = []
    rawWords = rawWordString.split(" ")
    for w in rawWords:
        noPunctString = re.sub(r'[^\w\s]', '', w).lower()
        noPunctWords.append(noPunctString)
    return noPunctWords

assert (example_input.split(" ")) == ['Aku', 'Suka', 'Suka']
assert (cleanwords(example_input)) == ['aku', 'suka', 'suka']

def findtranslations(rawWordString: str) -> dict:
    rawMalayWords = rawWordString.split(" ")
    cleanMalayWords = cleanwords(rawWordString)
    translationsDict = {}
    with open("malay_eng_dict.json", "r") as f:
        malayDict = json.load(f)
        for i in range(0, (len(cleanMalayWords))):
            if cleanMalayWords[i] in malayDict:
                translation = malayDict[cleanMalayWords[i]]
            else:
                translation = "n/a"
            translationsDict[rawMalayWords[i]] = translation
    return translationsDict

assert (findtranslations(example_input)) == {'Aku': 'me; I', 'Suka': 'like; enjoy', 'Suka': 'like; enjoy'}

