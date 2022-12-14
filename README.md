# malay-eng-dict
![example-image](https://github.com/Candyzorua/malay-eng-dict/blob/master/malay-eng-dict-example-image.jpeg?raw=true)

A web application to help English-speaking learners of Malay and Malay-speaking learners of English. 

Any chunk of Malay text can be inputted. After submitting, users can hover over any Malay word to view the English translation as a popover, if the English translation is available.

Completed, with some functionalities remaining to be added.

## HOW TO RUN:
- Ensure all packages denoted in requirements.txt are installed.
- Run find_translation_sentence_backend.py
- Open find_translation_sentence_frontend.html in your web browser.

## TODO:
- Host website on the cloud using Google App Services or another service provider.
- Fix bug where line breaks in the input are deleted in the output.
- Add GitHub and LinkedIn links.
- Look into connecting the Google Translate API to additionally show actual translation of the text chunk.
- Update malay-eng-dict.json with more dictionary entries.
- Enable users to login and keep a record of dictionary entries that they wish to remember.
- Implement fuzzy logic whereby translations of similar words are provided if the translation is 'n/a' for a particular Malay word.

## FILES:
- find_translation_sentence_frontend.html: uses Bootstrap for styling and vanilla JS for AJAX as well as the main functionality.
- find_translation_sentence_backend.py: a Flask API that interacts with the frontend and malay-eng-dict.json.
- get_translation_function.py: deals with malay-eng-dict.json; used in find_translation_sentence_backend.py.
- malay-eng-dict-obtainer.py: uses BeautifulSoup, Requests, and regex to scrape and clean data from http://dictionary.bhanot.net and returns malay-eng-dict.json.
- malay-eng-dict.json: a json file of Malay words and their English translations.
- styles.css: additional styling.

