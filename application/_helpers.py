from application.config import *

def load_config(MODE):
    try:
        if MODE == 'production':
            return ProductionConfig
        elif MODE == 'testing':
            return TestingConfig
        else:
            return DevelopmentConfig
    except EnvironmentError:
        raise EnvironmentError('Invalid environment for app state.')