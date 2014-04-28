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

life_inbox = tw.find_list('Life', 'Inbox')
if list is not None:
    tw.add_card(life_inbox, "hello", time.gmtime())
