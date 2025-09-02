# test_app.py
from app import insecure_eval

def test_insecure_eval():
    # Call the insecure function so CodeQL detects it
    assert insecure_eval("1 + 1") == 2
