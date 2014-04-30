# -*- coding: utf-8 -*-

import unittest
import trello_wrapper

from flask import Flask
from trello_wrapper import TrelloWrapper
import time
import pdb

class TrelloWrapperTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_pyfile('settings.cfg')

        self.tw = TrelloWrapper(
                self.app.config['TRELLO_API_KEY'],
                self.app.config['TRELLO_TOKEN'])

    def tearDown(self):
        pass

    def test_find_list(self):
        life_inbox = self.tw.find_list('Life', 'Inbox')
        self.assertIsNotNone(life_inbox,
                "test find_list failed.")

    def test_add_card(self):
        life_inbox = self.tw.find_list('Life', 'Inbox')
        if life_inbox is not None:
            self.tw.add_card(life_inbox, "hello", time.localtime())

    def test_smart_add_card(self):
        sentence = u'明天晚上19点打球#l'
        ret = self.tw.smart_add_card(sentence)
        self.assertTrue(ret, "test smart_add_card failed.")

if __name__ == '__main__':
    unittest.main()
