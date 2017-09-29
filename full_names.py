#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : full_names.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 29.09.2017
# Last Modified Date: 29.09.2017
# Last Modified By  : Channith Am <amcnith@gmail.com>

def get_full_name(first, last, middle=''):
    """Return a full name."""
    if middle:
        full_name = "{0} {1} {2}".format(first, middle, last)
    else:
        full_name = "{0} {1}".format(first, last)


    return full_name.title()
