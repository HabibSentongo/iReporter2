# import os

# class GeneralConfig:
#     DEBUG = False
#     TESTING = False
#     DB_URI = os.getenv('DATABASE_URL')
    

# class DevConfig(GeneralConfig):
#     DEBUG = True
#     ENV = 'dev_env'
#     DATABASE = 'iReporter_db'
#     TESTING = False


# class TestConfig(GeneralConfig):
#     DEBUG = True
#     ENV = 'test_env'
#     DATABASE = 'test_iReporter_db'
#     TESTING = True

# class DeployConfig(GeneralConfig):
#     DEBUG = False
#     ENV = 'deploy_env'
#     DATABASE_URI = 'postgres://nixbotuppxfnht:eb17041db3517c38f2479ea2c2f195ab65cc19718ceff3a903244f064e6b3507@ec2-54-227-246-152.compute-1.amazonaws.com:5432/derui7kb7ke7dv'
#     DATABASE = 'derui7kb7ke7dv'
#     HOST = 'postgres://nixbotuppxfnht:eb17041db3517c38f2479ea2c2f195ab65cc19718ceff3a903244f064e6b3507@ec2-54-227-246-152.compute-1.amazonaws.com:5432/derui7kb7ke7dv'
#     USER = 'nixbotuppxfnht'
#     PASSWORD = 'eb17041db3517c38f2479ea2c2f195ab65cc19718ceff3a903244f064e6b3507'
#     TESTING = False

# app_config_dict = {
#     'deploy':DeployConfig,
#     'test':TestConfig,
#     'dev':DevConfig
# }