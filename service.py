# -*- coding: utf-8 -*-
"""
    trello-service
    ~~~~~~~~~~~~~~

    A simple trello service for handling trello messages
    
    Copyright: (c) 2014 by Zhu Xiaoen.
"""

from flask import Flask
from trello import TrelloClient


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

tc = TrelloClient(app.config['TRELLO_API_KEY'],
        app.config['TRELLO_TOKEN'])

print(tc.list_boards())
