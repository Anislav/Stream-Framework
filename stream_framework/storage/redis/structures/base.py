from stream_framework.storage.redis.connection import RedisConnectionMixin
from redis.client import BasePipeline


class RedisCache(RedisConnectionMixin):

    '''
    The base for all redis data structures
    '''
    key_format = 'redis:cache:%s'

    def __init__(self, key, redis=None):
        # write the key
        self.key = key
        # handy when using fallback to other data sources
        self.source = 'redis'

    def get_key(self):
        return self.key

    def delete(self):
        key = self.get_key()
        self.redis.delete(key)

    def _pipeline_if_needed(self, operation, *args, **kwargs):
        '''
        If the redis connection is already in distributed state use it
        Otherwise spawn a new distributed connection using .map
        '''
        pipe_needed = not isinstance(self.redis, BasePipeline)
        if pipe_needed:
            pipe = self.redis.pipeline(transaction=False)
            operation(pipe, *args, **kwargs)
            results = pipe.execute()
        else:
            results = operation(self.redis, *args, **kwargs)
        return results
