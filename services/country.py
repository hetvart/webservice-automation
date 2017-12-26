from lib.client import ServiceClient

"""
This decorator modifies a dictionary response from the country service and
"""


def remove_duplicates_from_dataset_table(func):
    def wrapper(*args):
        res_dct = {}
        res = func(*args)
        for dct in res["NewDataSet"]["Table"]:
            for k, v in dct.items():
                if v not in res_dct.values():
                    res_dct[k] = v
        return res_dct

    return wrapper


class CountryService(object):
    def __init__(self, wsdl):
        self._client = ServiceClient(wsdl)

    @remove_duplicates_from_dataset_table
    def get_countries(self, code):
        return self._client.GetCountryByCurrencyCode(code)

    @remove_duplicates_from_dataset_table
    def get_country_by_country_code(self, code):
        return self._client.GetCountryByCountryCode(code)


c = CountryService("http://www.webservicex.net/country.asmx?wsdl")
print(c.get_countries('QAR'))
