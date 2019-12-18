from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


class CoreUtils(object):
    @classmethod
    def get_default_page_size(cls, key='DEFAULT_PAGE_SIZE'):
        '''
        functions to get default page size
        '''
        try:
            return getattr(settings, key)
        except Exception as exc:
            raise ImproperlyConfigured('%s is required' % key)

    @classmethod
    def get_default_page_index(cls, key='DEFAULT_PAGE_INDEX'):
        '''
        functions to get default page index
        '''
        try:
            return getattr(settings, key)
        except Exception as exc:
            raise ImproperlyConfigured('%s is required' % key)

    @classmethod
    def get_start_end_index(cls, page, limit):
        '''
        get start and end limit based on a pageIndex and pageSize
        '''
        start = page*limit
        end = start+limit
        return start, end, page, limit
