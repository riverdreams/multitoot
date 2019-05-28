# -*- coding: utf-8 -*-

from collections import namedtuple

__version__ = '0.21.0_0'

App = namedtuple('App', ['instance', 'base_url', 'client_id', 'client_secret'])
User = namedtuple('User', ['instance', 'username', 'access_token'])

DEFAULT_INSTANCE = 'mastodon.social'

CLIENT_NAME = 'multitoot - a Mastodon CLI client with multi-instance timeline merging'
CLIENT_WEBSITE = 'https://github.com/riverdreams/multitoot'
