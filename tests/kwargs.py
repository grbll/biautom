import json
dict_ = {"User" :{"Name" : [{"this": 2}, {"noot" : 3}], "ID" : 10, "Other" : {"ID" : 1}}}


class OurObject:
    def __init__(self, kwargs):
        self.__dict__.update(kwargs)

    # def __repr__(self):
    #     keys = sorted(self.__dict__)
    #     items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
    #     return "{}({})".format(type(self).__name__, ", ".join(items))
    #
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__
      
      
x = json.dumps(dict_)
y = json.loads(x, object_hook=lambda d: OurObject(d))

print(y.User.Name[1].nooot) 
