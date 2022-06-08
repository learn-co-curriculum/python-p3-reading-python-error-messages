#!/usr/bin/env python

import runpy

class TestNameError:
    '''
    a_name_error.py
    '''

    def test_name_error(self):
        '''
        contains defined name "hello_world"
        '''
        runpy.run_path('lib/a_name_error.py')
