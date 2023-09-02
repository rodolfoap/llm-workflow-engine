#!/usr/bin/env python

from lwe.core.config import Config
from lwe import ApiBackend

def test_api_backend_get_history():
    config = Config(profile='test')
    config.set('debug.log.enabled', True)
    config.set('backend_options.default_user', 1)
    config.set('database', 'sqlite:///$DATA_DIR/profiles/$PROFILE/storage.db')
    gpt = ApiBackend(config)
    success, history, user_message = gpt.get_history(limit=3)
    if success:
        print("\nHistory:\n")
        for id, conversation in history.items():
            print(conversation['title'])
    assert success

if __name__ == '__main__':
    test_api_backend_get_history()
