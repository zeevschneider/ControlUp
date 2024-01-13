import yaml


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class GetEnv:
    """
        Creates one and only instance of env data to be used across all test
    """
    def __init__(self):
        with open("../support/environment.yml", "r") as env:
            self.data = yaml.load(env, Loader=yaml.FullLoader)

    def get_env_data(self):
        return self.data
