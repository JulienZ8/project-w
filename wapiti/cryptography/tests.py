from django.test import TestCase
import unittest
from . import cipher_algorithms as ca


# Create your tests here.
class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher_27(self):
        result = ca.caesar_cipher(key=27, text="abc")
        expected_result = "bcd"
        self.assertEqual(result, expected_result)

    def test_caesar_cipher_53(self):
        result = ca.caesar_cipher(key=53, text="abc")
        expected_result = "bcd"
        self.assertEqual(result, expected_result)

    def test_caesar_cipher_special_char(self):
        result = ca.caesar_cipher(key=1, text="Salut, Yann clâvien!")
        expected_result = "Tbmvu, Zboo dmâwjfo!"
        self.assertEqual(result, expected_result)

    def test_one_time_pad_same_length(self):
        result = ca.one_time_pad(mask='xmckl', text='hello')
        expected_result = 'eqnvz'
        self.assertEqual(result, expected_result)


    def test_one_time_pad_mask_shorter(self):
        result = ca.one_time_pad(mask='xmckl', text='hellow')
        expected_result = 'eqnvzt'
        self.assertEqual(result, expected_result)
