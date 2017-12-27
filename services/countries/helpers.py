class ResponseObject(object):
    def __init__(self, dictionary):
        """
        Create an object from a dict with dict keys as attributes and values as attributes values

        :type dictionary: dict
        """
        for key in dictionary:
            setattr(self, key, dictionary[key])


def remove_duplicates_from_dataset_table(func):
    def wrapper(*args):
        """
        Remove duplicates objects from list of dictionaries and returns new dictionary

        :rtype: dict
        """
        res_dct = {}
        res = func(*args)
        for i in res["NewDataSet"]["Table"]:
            for k, v in i.items():
                if v not in res_dct.values():
                    res_dct[k] = v
        return res_dct

    return wrapper


def create_object_from_dict(func):
    def wrapper(*args):
        """
        Makes object from dictionary

        :rtype: ResponseObject
        """
        return ResponseObject(func(*args))

    return wrapper
