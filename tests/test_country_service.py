import unittest

from ddt import file_data, ddt, unpack
from tests.test_base import BaseTestCase


@ddt
class TestClass(BaseTestCase):
    @unpack
    @file_data('test_data.json')
    def test_qatar_scenario(self, country_name, country_code, country_currency, currency_code):
        # step1 getting country by its code
        country = self.service.get_country_by_country_code(country_code)
        self.assertEqual(country_name, country.name)

        # step2 getting country currency by country
        currency = self.service.get_currency_by_country(country.name)
        self.assertEqual(currency_code, currency.CurrencyCode)

        # step3 getting country by currency code
        country = self.service.get_country_by_currency_code(currency.CurrencyCode)
        self.assertEqual(country_currency, country.Currency)

        # step4 getting currency code by currency name
        currency = self.service.get_currency_code_by_currency_name(currency.Currency)
        self.assertIn(currency_code, currency.CurrencyCode)


if __name__ == "__main__":
    test_suites = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suites)
