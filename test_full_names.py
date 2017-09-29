#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : test_full_names.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 29.09.2017
# Last Modified Date: 29.09.2017
# Last Modified By  : Channith Am <amcnith@gmail.com>

import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Tests for names.py"""

    def test_first_last(self):
        """Test names like Janis Joplin"""
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

    def test_middle(self):
        """Test names like David Lee Roth"""
        full_name = get_full_name('david', 'roth', 'lee')

unittest.main()
