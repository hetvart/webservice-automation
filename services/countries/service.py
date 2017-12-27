from lib.client import ServiceClient
from services.countries.helpers import create_object_from_dict, remove_duplicates_from_dataset_table


class CountryService(object):
    def __init__(self, wsdl):
        self._client = ServiceClient(wsdl)

    def get_countries_list(self):
        return [d['Name'] for d in self._client.GetCountries()['NewDataSet']["Table"]]

    @create_object_from_dict
    @remove_duplicates_from_dataset_table
    def get_country_by_country_code(self, code):
        return self._client.GetCountryByCountryCode(code)

    @create_object_from_dict
    @remove_duplicates_from_dataset_table
    def get_currency_by_country(self, country_name):
        return self._client.GetCurrencyByCountry(country_name)

    @create_object_from_dict
    @remove_duplicates_from_dataset_table
    def get_country_by_currency_code(self, code):
        return self._client.GetCountryByCurrencyCode(code)

    @create_object_from_dict
    @remove_duplicates_from_dataset_table
    def get_currency_code_by_currency_name(self, name):
        return self._client.GetCurrencyCodeByCurrencyName(name)

