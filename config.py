import os

class GeneralConfig:
    DEBUG = False
    TESTING = False
    DB_URI = os.getenv('DATABASE_URL')
    

class DevConfig(GeneralConfig):
    DEBUG = True
    ENV = 'dev_env'
    DATABASE = 'iReporter_db'
    TESTING = False


class TestConfig(GeneralConfig):
    DEBUG = True
    ENV = 'test_env'
    DATABASE = 'test_iReporter_db'
    TESTING = False

class DeployConfig(GeneralConfig):
    DEBUG = False


app_config_dict = {
    'deploy':DeployConfig,
    'test':TestConfig,
    'dev':DevConfig

}