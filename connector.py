import json

def getTarea():
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        return data['tarea']

def getAsignatura():
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        return data['asignatura']

def getFecha():
    with open('data.json','r+') as json_file:
        data = json.load(json_file)
        return data['fecha']

def setJSON(x: str, y: str, z: str):
    with open('data.json','w') as json_file:
        data = {"tarea": x, "asignatura": y, "fecha": z}
        json.dump(data, json_file)
