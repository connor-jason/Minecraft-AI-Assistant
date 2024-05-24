import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, "app//View//static")
    TEMPLATE_FOLDER = os.path.join(basedir, "app//View//templates")
