from django.conf import settings
from api.models import Process, Recipe
import requests


class ProcessAPI(object):

    def get_url(self, process_id=None):
        url = settings.API_URL
        if process_id:
            url += "controlling/process/{}/".format(process_id)
        else:
            url += "controlling/process/"
        return url

    def filter_url(self, **kwargs):
        url = self.get_url() + '?'
        for arg, value in kwargs.items():
            url += arg + '=' + value + '&'
        return url

    def get_data(self, url):
        response = requests.get(url)
        return response.json()

    def post_data(self, url, data):
        requests.post(url, data=data)

    def get_current_process(self):
        url = self.filter_url(is_active='True')
        json_data = self.get_data(url)
        return json_data

    def all(self):
        data = self.get_data(self.get_url())
        data = data['objects']
        return self.create_process_list(data)

    def create_process(self, **kwargs):
        url = settings.API_URL + 'controlling/create/process/'
        return self.post_data(url, kwargs)

    def create_process_list(self, json_list):
        obj_list = []
        for obj in json_list:
            process = Process.create_obj(obj)
            obj_list.append(process)
        return obj_list


class RecipeAPI(object):

    def get_url(self, recipe_id=None):
        url = settings.API_URL
        if recipe_id:
            url += "controlling/recipe/{}/".format(recipe_id)
        else:
            url += "controlling/recipe/"
        return url

    def filter_url(self, **kwargs):
        url = self.get_url() + '?'
        for arg, value in kwargs.items():
            url += arg + '=' + value + '&'
        return url

    def get_data(self, url):
        response = requests.get(url)
        return response.json()

    def all(self):
        data = self.get_data(self.get_url())
        data = data['objects']
        return self.create_recipes_list(data)

    def create_recipes_list(self, json_list):
        obj_list = []
        for obj in json_list:
            recipe = Recipe.create_obj(obj)
            obj_list.append(recipe)
        return obj_list
