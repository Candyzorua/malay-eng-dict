# malay-eng-dict
A web application to help English-speaking learners of Malay and Malay-speaking learners of English. 

Any chunk of Malay text can be inputted. After submitting, users can hover over any Malay word to view the English translation as a popover, if the English translation is available.

Completed, with some functionalities remaining to be added.

## TODO:
- Host website on the cloud using Google App Services or another service provider.
- Fix bug where line breaks in the input are deleted in the output.
- Add GitHub and LinkedIn links.
- Update malay-eng-dict.json with more dictionary entries.
- Enable users to login and keep a record of dictionary entries that they wish to remember.

## FILES:
- find_translation_sentence_frontend.html: uses Bootstrap for styling and vanilla JS for AJAX as well as the main functionality.
- find_translation_sentence_backend.py: a Flask API that interacts with the frontend and malay-eng-dict.json.
- get_translation_function.py: deals with malay-eng-dict.json; used in find_translation_sentence_backend.py.
- malay-eng-dict-obtainer.py: uses BeautifulSoup, Requests, and regex to scrape and clean data from http://dictionary.bhanot.net and returns malay-eng-dict.json.
- malay-eng-dict.json: a json file of Malay words and their English translations.
- styles.css: additional styling.

