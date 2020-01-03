"""Server unit-tests"""


import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.constants import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import create_response


class TestServer(unittest.TestCase):
	"""
	Тесты функции сервера create_response()
	"""

	err_dict = {
		RESPONSE: 400,
		ERROR: 'Bad Request'
	}
	ok_dick = {RESPONSE: 200}

	def test_no_action(self):
		"""Ошибка при отсутствии поля ACTION"""
		self.assertEqual(create_response(
			{TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

	def test_wrong_action(self):
		"""Ошибка если значение ACTION неизвестно"""
		self.assertEqual(create_response(
			{ACTION: 'Any', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

	def test_no_time(self):
		"""Ошибка при отсутствии штампа времени"""
		self.assertEqual(create_response(
			{ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

	def test_no_user(self):
		"""Ошибка если нет пользователя"""
		self.assertEqual(create_response(
			{ACTION: PRESENCE, TIME: 1.1}), self.err_dict)

	def test_unknown_user(self):
		"""Ошибка если пользователь не Gest"""
		self.assertEqual(create_response(
			{ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)

	def test_ok_check(self):
		"""Проверка корректного запроса"""
		self.assertEqual(create_response(
			{ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dick)


if __name__ == '__main__':
	unittest.main()
