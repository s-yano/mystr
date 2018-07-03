# -*- coding: utf-8 -*-

from unittest import TestCase, main
from mystr import to_upper

class ToUpperTestCase(TestCase):
    def test_to_upper(self):
        self.assertEqual('ABCDEFGHI123', to_upper('abcDEFghi123'))

if __name__ == '__main__':
    main()
