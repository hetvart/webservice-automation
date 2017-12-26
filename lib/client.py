from json import dumps, loads
import xmltodict
from zeep import Client


class ServiceClient(object):
    def __init__(self, wsdl):
        self._client = Client(wsdl).service

    def __getattr__(self, item):
        operation = self._client.__getattr__(item)

        res_dct = {}

        def wrapper(*args):
            result = operation(*args)
            parsed = loads(dumps(xmltodict.parse(result)))

            if item in ('GetCountries', 'GetCurrencies', 'GetCurrencyCode'):
                return parsed["NewDataSet"]["Table"]

            for dct in parsed["NewDataSet"]["Table"]:
                for k, v in dct.items():
                    if v not in res_dct.values():
                        res_dct[k] = v
            return res_dct

        return wrapper
