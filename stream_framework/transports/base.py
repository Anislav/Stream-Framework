from stream_framework.serializers.transport.base import JSONSerializer


class BaseTransport(object):

    '''
    BaseTransport class provides an interface for sending data over the wire.
    It uses a serializer_class to create a message from the input data
    that could be transported.

    This class defines the signature of the send_message method that must be implemented
    by every successor class.
    '''

    # : serializer class to use for converting the data into a message that could be transported
    serializer_class = JSONSerializer

    def __init__(self, feed_key):
        self.feed_key = feed_key
        self.serializer = self.serializer_class()

    def create_message(self, data):
        '''
        Using a serializer creates a message from the provided data
        that is suitable for transportation.

        :param data: data to be serialized into a message that could be transported
        '''
        message = self.serializer.dumps(dict(data=data,
                                             feed_key=self.feed_key))
        return message

    def send_message(self, message):
        '''
        This method is responsible for the actual transportation of the created message.
        It must be implemented by every successor class.

        :param message: a message that is suitable for transportation
        '''
        raise NotImplemented

    def send_data(self, data):
        '''
        Serializes the provided data into a message and then transports it.

        :param data: data to be serialized and transported
        '''
        message = self.create_message(data)
        self.send_message(message)
