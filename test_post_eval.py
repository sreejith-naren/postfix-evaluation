from postfix_evaluation import post_eval

def test_emptylist():
    assert post_eval("")== None

def test_proper():
    assert post_eval("231+-")== 2    

def test_special_char():
    assert post_eval("!@#$%")== None

def test_isalpha():
    assert post_eval("abcdefg")== None    