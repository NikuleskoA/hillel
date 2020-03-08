import os
import json

class JsonFile:
    def write(self, dict1, fname:str):
        file1 = open(fname, 'w')
        json.dump(dict1, file1, )
        file1.close()

    def read(self, fname:str):
        file1 = open(fname, 'r')
        line = file1.readline()
        while line:
            print(line)
            line = file1.readline()
        file1.close()

    def unite(self, filenames: list):
        dict1 = dict()
        for file in filenames:
            file1 = open(str(file),'r')
            dict1.update(json.load(file1))
            file1.close()
        u_file = open("ufile.json", "w")
        json.dump(dict1, u_file)
        u_file.close()

    def abs_path(self, filename: str):
        return os.path.abspath(filename)

    def rel_path(self, filename: str):
        return os.path.relpath(filename)


json1 = JsonFile()
data = {
   "firstName": "Alex",
   "lastName": "Brown",
   "address": {
       "streetAddress": "Korol'ova St., 57",
       "city": "Odessa",
       "postalCode": 65000
   }
}
data1 = {
   "address": {
       "streetAddress": "Zelena St.",
       "city": "Kyiv",
       "postalCode": 32300
   },
    "unnecessary info": "NONE"
}
json1.write(data, "data.json")
json1.read("data.json")
json1.write(data1, "data1.json")
json1.read("data1.json")
json1.unite(["data.json", "data1.json"])
json1.read("ufile.json")
print("Aбсолютный путь: ", json1.abs_path("ufile.json"))
print("Относительный путь: ", json1.rel_path("ufile.json"))

