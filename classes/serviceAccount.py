from functools import singledispatchmethod
import json


class serviceAccount:
    def __init__(self, id=0, description='', app='', project=''):
        self.id = id  # number of service account
        self.description = description  # description
        self.app = app  # Application id eg. APP0000
        self.project = project  # Project id

    
    def show(self):
        print(
            f'service account id: {self.id}, application: {self.app}, project {self.project}')

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def check(self):
        if len(self.app) < 1: 
            raise TypeError(f'Not set application id')
        if len(self.project) < 1: 
            raise TypeError(f'Not set project name')




class list_of_serviceAccount:
    def __init__(self):
        self.list = []  # list of service accounts
        self.file = 'serviceAccount.json'  # path to service accounts
        self.number_max = 9999


    def add(self, app: str, project: str, description: str):
        id = self.free_id(project)
        sa = serviceAccount(id, description, app, project)
        self.list.append(sa)

    def delete(self, id: int, project: str):
        sa = [sa for sa in self.list if sa.id == id and sa.project == project]
        self.list.remove(sa[0])

    def free_id(self, project: str):
        list_of_id = [sa.id for sa in self.list if sa.project == project]
        free_id = [i for i in range(self.number_max) if i not in list_of_id]
        return free_id[0]

    def load(self):
        try:
            with open(self.file, 'r') as outputfile:
                json_object = json.load(outputfile)
                list_of_sa = [json.loads(sa) for sa in json_object]
        except:
            raise TypeError(f'Unrecognized file {self.file}')

        self.list = [serviceAccount(
            int(sa['id']), sa['description'], sa['app'], sa['project']) for sa in list_of_sa]

    def save(self):
        list = [sa.toJSON() for sa in self.list]
        with open(self.file, "w") as outfile:
            json.dump(list, outfile)

    def show(self):
        if len(self.list) < 1:
            print('Empty list')
        [sa.show() for sa in self.list]
