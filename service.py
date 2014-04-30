# -*- coding: utf-8 -*-
"""
    trello-service
    ~~~~~~~~~~~~~~

    A simple trello service for handling trello messages
    
    Copyright: (c) 2014 by Zhu Xiaoen.
"""

from flask import Flask
from trello_wrapper import TrelloWrapper
import time
import sys


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

tw = TrelloWrapper(app.config['TRELLO_API_KEY'],
        app.config['TRELLO_TOKEN'])

if __name__ == '__main__':
    sentence = sys.argv[1].decode('utf-8')
    ret = tw.smart_add_card(sentence)
    if ret is True:
        print("Add card to trello success.")
    else:
        print("Add card to trello failed.")
