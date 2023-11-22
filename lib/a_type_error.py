# lib_test.py

import pytest
import lib.a_type_error  # Import the module directly

class TestTypeError:
    def test_type_error(self):
        '''
        adds two numbers
        '''
        with pytest.raises(TypeError):
            lib.a_type_error.wrong_type = 'abc' + str(123)
