# This file is part asset_internetdomain module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AssetInternetdomainTestCase(ModuleTestCase):
    'Test Asset Internetdomain module'
    module = 'asset_internetdomain'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AssetInternetdomainTestCase))
    return suite
