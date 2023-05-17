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
            ("-40 / 36 - 36 + -95 / -69 + 82 / 50 - 33", -67.09429951690822),
            ("-13 - 100 - 78 / 38 * -85 / 27 / -19 - -45", -68.34010464758387),
            ("(8) + (-1 * 29 - (65)) / (-28 + -(((-(-16 + 65)))) + 74)",  7.010526315789473),
            ("(37) / (-73 * -87 - -(4)) - (62 - ((((3 - 96)))) * 30)",  -2851.994177812746),
            ("(-98) * (100 + -60 - (69)) + (94 - -(((-(22 - -45)))) * -96)",  9368),
            ("(71) - (13 + -33 - -(65)) - (-95 - ((((-47 + -62)))) / 2)", 66.5),
            ("-(-39) - (41 / -27 - (14)) * (50 - -(((-(96 * 91)))) * -3)", 407524.25925925927),
            ("-(51) + (-68 / -50 + -(39)) / (-84 - (((-(99 * -47)))) * -27)", -51.00029980804002))

    no_of_tests = 0
    no_of_successful_tests = 0   
    for case in cases:
        my_solution = calc(case[0])
        try:
            no_of_tests += 1
            assert my_solution == case[1], f"FAILED!!!!!!!!!!: Expression {case[0]} returned {my_solution} instead of {case[1]}"
            print("{} = {} PASS!".format(my_solution, case[1]))
            no_of_successful_tests += 1
        except AssertionError as e:
            print(e)
    print("Final report: {} test evaluated, {} succeeded, {} failed".format(no_of_tests, no_of_successful_tests, no_of_tests - no_of_successful_tests))
        
test()