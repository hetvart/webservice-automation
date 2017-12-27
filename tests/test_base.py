import unittest

from global_settings import BASE_URL
from services.countries.service import CountryService


class BaseTestCase(unittest.TestCase):

    SERVICE_URL = BASE_URL

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        cls.service = CountryService(cls.SERVICE_URL)
