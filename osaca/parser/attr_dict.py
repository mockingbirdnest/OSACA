#!/usr/bin/env python3


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @staticmethod
    def convert_dict(dictionary):
        if isinstance(dictionary, type(list())):
            return [AttrDict.convert_dict(x) for x in dictionary]
        if isinstance(dictionary, type(dict())):
            for key in list(dictionary.keys()):
                entry = dictionary[key]
                if isinstance(entry, type(dict())) or isinstance(
                    entry, type(AttrDict())
                ):
                    dictionary[key] = AttrDict.convert_dict(dictionary[key])
                if isinstance(entry, type(list())):
                    dictionary[key] = [AttrDict.convert_dict(x) for x in entry]
            return AttrDict(dictionary)
        return dictionary