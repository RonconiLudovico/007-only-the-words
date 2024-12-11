import unittest

from main import de_punct, main

class Test1(unittest.TestCase):
    def test_depunct(self):
        '''
        Here we test the function de_punct
        '''
        data = "Hello! .,!:; what?"
        result = de_punct(data)
        self.assertEqual(["H", "e", "l", "l", "o", " ", " ", "w", "h", "a", "t"], result)


class Test2(unittest.TestCase):
    def test_depunct(self):
        '''
        Here we test the function de_punct
        '''
        data = "!.,!:;what?"
        result = de_punct(data)
        self.assertEqual(["w", "h", "a", "t"], result)


class Test3(unittest.TestCase):
    def test_depunct(self):
        '''
        Here we test the function de_punct
        '''
        data = ".,:;-f?u!n'zi-a!"
        result = de_punct(data)
        self.assertEqual(["f", "u", "n", "z", "i", "a"], result)


class Test4(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the function main
        '''
        data = "Hello! .,!:; what?"
        result = main(data)
        self.assertEqual('Hello  what', result)


class Test5(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the function main
        '''
        data = "This. Is my program! I, am, your creator."
        result = main(data)
        self.assertEqual('This Is my program I am your creator', result)


class Test6(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the function main
        '''
        data = ":) -.- oh god ;) ._. ?.? !.!"
        result = main(data)
        self.assertEqual(')  oh god ) _  ', result)


