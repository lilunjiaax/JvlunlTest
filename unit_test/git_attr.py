
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            return KeyError('not have this attribute %s' % item)

    def __setattr__(self, key, value):
        self[key] = value





