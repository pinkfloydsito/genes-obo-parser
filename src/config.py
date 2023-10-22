import os
from decouple import Config, RepositoryEnv

config = None

if os.environ.get('DEVELOPMENT'):
    config = Config(RepositoryEnv('.env.dev'))
elif os.environ.get('TEST'):
    config = Config(RepositoryEnv('.env.test'))
else:
    raise ValueError("Specify DEVELOPMENT or TEST environment.")