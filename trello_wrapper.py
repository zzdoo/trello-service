# -*- coding: utf-8 -*-
"""A wrapper for py-trello, add due time support"""

from trello import TrelloClient
import time


class TrelloWrapper():
    def __init__(self, api_key, api_token):
        self.tc = TrelloClient(api_key, api_token)


    def add_card(self, list_target, card_name, card_due, desc=None):
        """
        Add card to list with a due date
            due: time.stuct_time object
        """
        try:
            due_str = time.strftime("%Y-%m-%dT%H:%M", card_due)
            json_obj = list_target.client.fetch_json(
                '/lists/' + list_target.id + '/cards',
                http_method='POST',
                post_args={'name': card_name, 'due': due_str,
                    'idList': list_target.id, 'desc': desc}, )
        except Exception as e:
            print(str(e))


    def find_list(self, board_name, list_name):
        """ Return list specified by board_name/list_name"""
        for b in self.tc.list_boards():
            if b.name != board_name:
                continue

            for l in b.open_lists():
                if l.name != list_name:
                    continue

                return l

        return None
