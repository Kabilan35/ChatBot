# BOSS FAQ Bot with Rasa-NLU
Set of scripts to build a chatbot which will answer FAQ about Bharat Operating System Solutions

## Scripts:
* app.py: Chatbot UI built using Flask, using templates/*.html
* engine.py: Chatbot core logic as well as knowledgebase.
* config.json: Rasa NLU settings for training as well as executing intent extraction
* run_training: Windows batch file to build trained modeling
* run_server: Windows batch file to execute Rasa-NLU server.

## Dependencies:
* Needs Python 3.5+
* rasa-nlu and rasa-core packages

## ToDos
* Add more training data
* Entity extraction not working as desired, find out more.
* Etc.

## References
* Rasa-NLU [installation](https://github.com/RasaHQ/rasa_nlu)

##Warning
* The code was trained by rasa-nlu. Thus only questions which are given accoring to the training data will get the desired output.
