from unittest import TestCase
from main import get_name, get_shelf, get_animals, documents, get_list

class TestSomething(TestCase):
    def test_get_name_ok(self):
        a = "11-2"
        exp = "Геннадий Покемонов"
        result = get_name(a)
        self.assertEqual(result, exp)

    def test_get_name_fail(self):
        a = "11-3"
        exp = "Геннадий Покемонов"
        result = get_name(a)
        self.assertEqual(result, exp)

    def test_shelf_ok(self):
        a = "11-2"
        exp = "Документ", "11-2", "лежит на полке номер ", "1"
        result = get_shelf(a)
        self.assertEqual(result, exp)

    def test_shelf_fail(self):
        a = "10006"
        exp = "Документ", "11-2", "лежит на полке номер ", "3"
        result = get_shelf(a)
        self.assertEqual(result, exp)

    def test_list_ok(self):
        a = documents
        exp = ["passport", "2207 876234", "Василий Гупкин", "invoice", "11-2", "Геннадий Покемонов", "insurance", "10006", "Аристарх Павлов"]
        result = get_list(a)
        self.assertEqual(result, exp)

    def test_list_fail(self):
        a = documents
        exp = ["passport", "2207 81176234", "Василий Гупкин", "invoice", "11-112", "Геннадий Покемонов", "insurance", "1110006", "Аристарх Павлов"]
        result = get_list(a)
        self.assertEqual(result, exp)


    def test_get_animals_ok(self):
        num = 2008
        exp = "Крыса"
        result = get_animals(num)
        self.assertEqual(result, exp)


    def test_get_animals_fail(self):
        num = 2008
        exp = "Петух"
        result = get_animals(num)
        self.assertEqual(result, exp)