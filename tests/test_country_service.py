import unittest

from lib.client import ServiceClient
# from services.country import CountryService


class BaseTestCase(unittest.TestCase):

    SERVICE_URL = "http://www.webservicex.net/country.asmx?wsdl"

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        # cls.service = CountryService(cls.SERVICE_URL)
        cls.service = ServiceClient(cls.SERVICE_URL)


class TestClass(BaseTestCase):
    def test_qatar_scenario(self):
        test_data = {
            "country name": "Qatar",
            "country code": "qa",
            "country currency": "Rial",
            "currency code": "QAR",
        }

        # step1 getting country by its code
        country_info = self.service.GetCountryByCountryCode(test_data['country code'])
        self.assertEqual(test_data['country name'], country_info['name'])

        # step2 getting country currency by country
        country_currency_info = self.service.GetCurrencyByCountry(country_info['name'])
        self.assertEqual(test_data['country currency'], country_currency_info['Currency'])
        # print(country_currency_info)

        # step3 getting country by currency code
        country_info = self.service.GetCountryByCurrencyCode(country_currency_info['CurrencyCode'])
        self.assertEqual(test_data['country name'], country_info['Name'])

        # step4 getting currency code by currency name
        currency_code = self.service.GetCurrencyCodeByCurrencyName(country_info['Currency'])
        self.assertIn('CurrencyCode', currency_code)


if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
