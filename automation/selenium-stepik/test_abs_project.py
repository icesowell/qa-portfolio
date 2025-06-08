import unittest

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


#Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно.


#тот же код но с unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__": #Cлужит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля

    unittest.main()
    test_abs1()
    test_abs2()
    print("Everything passed!")
