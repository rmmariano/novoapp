#!/usr/bin/env python
# -*- coding: utf-8 -*-

from w2ptests import W2PTestCase

import default

# Testes relacionado ao Controlador Default
class TestCtlDefault(W2PTestCase):
	def setUp(self):
		W2PTestCase.setUp(self,default)

	def test_cfib(self):
		self.assertEqual(default.cfib()['message'],'5')
		#self.assertEqual(default.cfib()['message'],'55')
	def test_text(self):
		self.assertEqual(default.ctext()['text'],'Text')

# Não necessita do main() do unittest aqui, pois este arquivo será
# chamado pelo run_tests.py