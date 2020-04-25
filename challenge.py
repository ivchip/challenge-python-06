def make_division_by(n):
    def repeater(val):
        return val / n
    return repeater


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.value_18 = 18
            self.value_100 = 100
            self.value_54 = 54

        def test_closure_make_division_by_3(self):
            division_by_3 = make_division_by(3)
            self.assertEqual(6, division_by_3(self.value_18))

        def test_closure_make_division_by_5(self):
            division_by_5 = make_division_by(5)
            self.assertEqual(20, division_by_5(self.value_100))

        def test_closure_make_division_by_18(self):
            division_by_18 = make_division_by(18)
            self.assertEqual(3, division_by_18(self.value_54))

        def tearDown(self):
            del(self.value_18)
            del(self.value_100)
            del(self.value_54)
    
    run()
    unittest.main()
