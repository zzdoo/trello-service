# -*- coding: utf-8 -*-

import unittest
import parser
import time, datetime
import pdb

class ParserTest(unittest.TestCase):

    def setUp(self):
        self.t = time.time()
        self.date = datetime.datetime.fromtimestamp(self.t)
        self.parser = parser.Parser(self.t)
        pass

    def tearDown(self):
        pass

    def testFoo(self):
        self.assertEqual(1, 1, "testFoo fail")

    def test_parse_week_offset(self):
        sentence = u"周六去春游"
        offsets = [6, 5, 4, 3, 2, 1, 0, -1]
        self.assertEqual(self.parser.parse_week_offset(sentence),
                offsets[self.date.isocalendar()[2]],
                "parse_week_offset failed")

    def test_parse_day_offset(self):
        sentence = u"打算明天去春游"
        self.assertEqual(self.parser.parse_day_offset(sentence),
                1, "parse_day_offset failed")

    def test_parse_moment(self):
        sentence = u"晚上吃夜宵"
        self.assertEqual(self.parser.parser_moment(sentence),
                20, "parser_moment failed")

    def test_parse_clock(self):
        sentence = u"7点晨跑"
        self.assertEqual(self.parser.parser_clock(sentence),
                7, "parser_clock failed")

        sentence = u"19点吃饭"
        result = self.parser.parser_clock(sentence)
        self.assertEqual(result,
                19, "parser_clock failed, result:" + str(result))

        sentence = u"19点半吃饭"
        result = self.parser.parser_clock(sentence)
        self.assertEqual(result,
                19.5, "parser_clock failed, result:" + str(result))

    def test_parse_due_time(self):
        sentence = u"明天19点打球"
        dt = self.parser.parse_due_time(sentence)
        self.assertEqual(dt.hour, 19, "parse hour failed.")
        new_dt = self.date + datetime.timedelta(days=1)
        self.assertEqual(dt.day, new_dt.day)

    def test_parse_list(self):
        sentence = u"明天19点打球#l"
        (b, l) = self.parser.parse_list(sentence)
        self.assertTupleEqual((b, l), ("Life", "Inbox"),
                "test parse list test failed.")

if __name__ == '__main__':
    unittest.main()

