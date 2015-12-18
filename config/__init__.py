# -*- coding:utf-8 -*-
import importlib

# use development by default
config = {
    'development': ['development', 'DevelopmentConfig'],
    'testing': ['testing', 'TestingConfig'],
    'production': ['production', 'ProductionConfig'],
    'default': ['development_sample', 'DevelopmentConfig'],
}


def load_default():
    import development_sample
    return development_sample.DevelopmentConfig


def load_config(config_name):
    """Load config."""
    # error check. usually caused by error mode config
    if config_name not in config:
        print 'error! config mode {} not exists'.format(config_name)
        return None

    module, meth_name = config[config_name]
    try:
        config_module = importlib.import_module(module)
    except ImportError:
        print 'error! file "{}.py" not exists'.format(module)
    else:
        return getattr(config_module, meth_name)
    return None
