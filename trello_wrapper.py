# -*- coding: utf-8 -*-
"""A wrapper for py-trello, add due time support"""

from trello import TrelloClient
import time


class TrelloWrapper():
    def __init__(self, api_key, api_token):
        self.tc = TrelloClient(api_key, api_token)

    def add_card_with_due(self, name, due, desc=None):
        """
        Add card with a due date
            due: time.stuct_time object
        """

        # XXX Better methods to get list id
        # TODO Extract Life/Inbox as param
        for b in self.tc.list_boards():
            if b.name != 'Life':
                continue

            for l in b.open_lists():
                if l.name != 'Inbox':
                    continue
                try:
                    due_str = time.strftime("%Y-%m-%dT%H:%M", due)
                    json_obj = l.client.fetch_json(
                        '/lists/' + l.id + '/cards',
                        http_method='POST',
                        post_args={'name': name, 'due': due_str,
                            'idList': l.id, 'desc': desc}, )
                except Exception as e:
                    print(str(e))

