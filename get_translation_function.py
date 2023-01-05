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
        index = 0 
        #each dictionary entry must have an index, to prevent the keys for two entries for the same word from
        #being exactly alike, which will cause problems whem the dictionary is parsed into a JavaScript object
        for i in range(0, (len(cleanMalayWords))):
            index += 1
            if cleanMalayWords[i] in malayDict:
                translation = malayDict[cleanMalayWords[i]]
            else:
                translation = "n/a"
            translationsDict[index] = [translation, rawMalayWords[i]]
    return translationsDict

assert (findtranslations(example_input)) == {1: ['me; I', 'Aku'], 2 : ['like; enjoy', 'Suka'], 3 : ['like; enjoy', 'Suka']}

