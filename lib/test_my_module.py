# test_my_module.py

import my_module

def test_add():
    assert my_module.add(2, 3) == 5
    assert my_module.add(0, 0) == 0
    assert my_module.add(-1, 1) == 0
