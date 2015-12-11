# -*- coding:utf-8 -*-
import importlib

# use development by default
config = {
    'development': ['development', 'DevelopmentConfig'],
    'testing': ['testing', 'TestingConfig'],
    'production': ['production', 'ProductionConfig'],
    'default': ['development', 'DevelopmentConfig'],
}


def load_config(config_name):
    """Load config."""
    # error check. usually caused by error mode config
    if config_name not in config:
        print 'config error. {} not exists'.format(config_name)
        return

    module, meth_name = config[config_name]
    try:
        config_module = importlib.import_module(module)
    except ImportError:
        print 'import config error. file "{}.py" not exists'.format(module)
    else:
        return getattr(config_module, meth_name)
