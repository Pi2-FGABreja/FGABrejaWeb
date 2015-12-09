from datetime import datetime
from monitoring.states import get_stage, get_state


class Recipe(object):

    def __init__(self):
            self.name = ''
            self.description = ''
            self.malt = ''
            self.malt_weight = ''
            self.yeast = ''

    @classmethod
    def create_obj(cls, data):
        obj = cls()
        for attr in obj.__dict__.keys():
            value = data.get(attr)
            setattr(obj, attr, value)
        return obj


class Process(object):

    def __init__(self):
            self.initial_datetime = ""
            self.final_datetime = ""
            self.iodine_test = ""
            self.malt = ""
            self.state = ""
            self.is_active = ""
            self.recipe = ""

    def get_stage(self):
        return get_stage(self.state)

    @classmethod
    def create_obj(cls, data):
        obj = cls()
        for attr in obj.__dict__.keys():
            if data.get(attr) is None:
                value = data.get(attr)
            elif attr == "initial_datetime" or attr == "final_datetime":
                value = data.get(attr)
                value = value.split('.')[0]
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
            elif attr == "recipe":
                recipe = Recipe.create_obj(data[attr])
                value = recipe
            elif attr == "state":
                value = get_state(data[attr])
            else:
                value = data.get(attr)

            setattr(obj, attr, value)
        return obj
