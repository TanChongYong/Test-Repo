'test module' 
 
#from app.py import total   # The code to test
import pytest 
from app import home

def test_increment():
    assert home() == "Hello, Flask!"
