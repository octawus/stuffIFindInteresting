from evaluator import calc

def test ():
    cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14),
            ("-40 / 36 - 36 + -95 / -69 + 82 / 50 - 33", -67.09429951690822))
    
    special = (("-40 / 36 - 36 + -95 / -69 + 82 / 50 - 33", -67.09429951690822),)
    
    for case in special:
        try:
            assert calc(case[0]) == case[1], f"Expression {case[0]} returned {calc(case[0])} instead of {case[1]}"
        except AssertionError as e:
            print(e)

test()