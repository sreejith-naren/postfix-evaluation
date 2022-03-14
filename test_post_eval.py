from postfix_evaluation import post_eval

def test_not_enough_operands():
    assert post_eval("42351-+*+*")== 0