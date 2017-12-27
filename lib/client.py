from json import dumps, loads

import sys
import xmltodict
from zeep import Client


class ServiceClient(object):
    """
    That is a wrapper over the original zeep.Client
    """
    def __init__(self, wsdl):
        self._client = Client(wsdl).service

    def __getattr__(self, item):
        """
        Returns a converted dict response body instead of xml-based string

        :type item: zeep.client.OperationProxy
        :return: dict
        """
        try:
            operation = self._client.__getattr__(item)

            def wrapper(*args):
                result = operation(*args)
                if isinstance(result, str):
                    parsed = loads(dumps(xmltodict.parse(result)))
                    return parsed
                return result

            return wrapper
        except AttributeError:
            sys.exit("The service does not support the requested operation: %s." % item)
