import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    # Base Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    CSRF_ENABLED = True
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    DEBUG = os.getenv('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    
class ProductionConfig(BaseConfig):
    # Production Configuration   
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
    
class TestingConfig(BaseConfig):
    # Test Configuration
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
    PRESERVE_CONTEXT_ON_EXCEPTION = False