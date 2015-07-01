from stream_framework.storage.redis.connection import RedisConnectionMixin
from stream_framework.transports.base import BaseTransport


class RedisTransport(RedisConnectionMixin, BaseTransport):

    '''
    Transports data to a Redis Pub/Sub channel.

    '''

    # : The Redis Pub/Sub channel to send data to
    channel = ''

    def send_message(self, message):
        '''
        Sends the message to a Redis Pub/Sub channel.
        '''
        self.redis.publish(self.channel, message)
