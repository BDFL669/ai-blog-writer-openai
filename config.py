##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
