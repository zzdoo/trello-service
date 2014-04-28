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


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

tw = TrelloWrapper(app.config['TRELLO_API_KEY'],
        app.config['TRELLO_TOKEN'])

tw.add_card_with_due("hello", time.gmtime())
