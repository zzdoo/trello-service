# -*- coding: utf-8 -*-
"""A wrapper for py-trello, add due time support"""

from trello import TrelloClient
import time
import parser

class TrelloWrapper():
    def __init__(self, api_key, api_token):
        self.tc = TrelloClient(api_key, api_token)


    def add_card(self, list_target, card_name, card_due, desc=None):
        """
            Add card to list with a due date
            card_due: time.stuct_time object,
            use time.localtime()
        """
        try:
            # Convert to UTC datetime object
            card_due_utc = time.gmtime(time.mktime(card_due))
            due_str = time.strftime("%Y-%m-%dT%H:%M", card_due_utc)
            json_obj = list_target.client.fetch_json(
                '/lists/' + list_target.id + '/cards',
                http_method='POST',
                post_args={'name': card_name, 'due': due_str,
                    'idList': list_target.id, 'desc': desc}, )
        except Exception as e:
            print(str(e))


    def smart_add_card(self, sentence):
        """Check date keywords in the sentence,
        and use as card's due date."""
        # TODO Life/Inbox as default, move to config
        target_default = ("Life", "Inbox")
        t_curr = time.time()
        p = parser.Parser(t_curr)

        target = p.parse_list(sentence)
        if target is None:
            target = target_default
        due = p.parse_due_time(sentence)

        list_target = self.find_list(target[0],
                target[1])

        if list_target is None:
            return False

        self.add_card(list_target, sentence, due.timetuple())
        return True


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
