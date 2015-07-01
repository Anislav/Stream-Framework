import json


class BaseSerializer(object):

    '''
    The purpose of this class is to serialize data into message that
    could be sent by a transport class.

    BaseSerializer only defines the signature for dumps method.
    '''

    def dumps(self, data):
        '''
        Serializes a data into a message that is suitable for transportation.

        :param data: data to be serialized into a message that could be transported
        '''
        raise NotImplemented


class JSONSerializer(BaseSerializer):

    '''
    Serializes the provided data into a JSON representation.
    '''

    def dumps(self, data):
        return json.dumps(data)
