from django.test import TestCase
import unittest
from. import views

# Create your tests here.
class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher_27(self):
        result = views.caesar_cipher(key=27, text="abc")
        expected_result = "bcd"
        self.assertEqual(result, expected_result)


    def test_caesar_cipher_53(self):
        result = views.caesar_cipher(key=53, text="abc")
        expected_result = "bcd"
        self.assertEqual(result, expected_result)

    def test_caesar_cipher_special_char(self):
        result = views.caesar_cipher(key=1, text="Salut, Yann clâvien!")
        expected_result = "Tbmvu, Zboo dmâwjfo!"
        self.assertEqual(result, expected_result)
