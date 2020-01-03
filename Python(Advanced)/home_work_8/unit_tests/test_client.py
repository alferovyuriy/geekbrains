"""
Client unit-tests
"""


import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.constants import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_message, get_answer


class TestClient(unittest.TestCase):
	"""Тесты функций клиента"""

	def test_def_message(self):
		"""Тест коректного запроса"""
		test = create_message(PRESENCE)
		test[TIME] = 1.1
		self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

	def test_type_message(self):
		"""Тест типа данных исходящего сообщения"""
		message = create_message(PRESENCE)
		message[TIME] = 1.1
		self.assertIsInstance(message, dict)

	def test_200_ans(self):
		"""Тест создания корректного ответа 200"""
		self.assertEqual(get_answer({RESPONSE: 200}), '200 : OK')

	def test_400_ans(self):
		"""Тест создания корректного ответа 400"""
		self.assertEqual(get_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

	def test_no_response(self):
		"""Тест исключения при отстутсвии поля RESPONSE"""
		self.assertRaises(ValueError, get_answer, {ERROR: 'Bad Request'})

	def test_wrong_type_message(self):
		"""Тест исключения при неверном типе данных входящего сообщения"""
		self.assertRaises(TypeError, get_answer, [RESPONSE])


if __name__ == '__main__':
	unittest.main()
