# This file is part sale_advance_payment_es module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class SaleAdvancePaymentEsTestCase(ModuleTestCase):
    'Test Sale Advance Payment Es module'
    module = 'sale_advance_payment_es'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            SaleAdvancePaymentEsTestCase))
    return suite
