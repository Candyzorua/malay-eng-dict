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

malay-eng-dict-obtainer.py: A web scraping program scrapes http://dictionary.bhanot.net and returns malay-eng-dict.json.

malay-eng-dict.json: a json file of Malay words and their English translations.

