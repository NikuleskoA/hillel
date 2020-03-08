import zipfile
import os
import itertools

letters = []
for letter in range(ord("a"), ord("z") + 1):
    letters.append(chr(letter))
password = list(itertools.product(letters, repeat=3))
z = zipfile.ZipFile("lesson6.zip", 'r')
print("Идет поиск пароля")
for i in password:
    try:
        r_password = str(i[0]+i[1]+i[2])
        z.extractall(pwd=r_password.encode("utf8"))
        break
    except:
        pass
print("Пароль архива: '{}'".format(r_password))
z.printdir()
z.close()

all_files_paths = []
for d, dirs, files in os.walk('lesson6'):
    for f in files:
        path = os.path.join(d, f)
        all_files_paths.append(path)

city_set = set()
dict1=dict()
os.mkdir("cities")
for file in all_files_paths:
    f = open(file.encode("utf8"), "r", errors='ignore')
    line = f.readline()
    while line:
        city = line.split('\t')[3]
        user_id = line.split('\t')[4]
        search_keyword = line.split('\t')[5]
        if dict1.get(user_id, search_keyword)!=city:
            dict1[(user_id, search_keyword)] = city
        if city not in city_set:
            a = open("cities//{}.tsv".format(city), 'w')#запускал на маке поэтому директория с таким слешом /
            a.close()
            city_set.add(city)
        line = f.readline()
    f.close()
count_dict = dict()
for city in city_set:
    for key in dict1:
        if dict1[key] == city:
            if key[1] not in count_dict:
                count_dict[key[1]] = 1
            else:
                count_dict[key[1]] += 1

    a = open("cities//{}.tsv".format(city),'a')
    for key in count_dict:
        a.write(key + "\t" + str(count_dict.get(key)) + "\n")
    a.close()
    count_dict.clear()
print("В папке cities для каждого города который встретился в логах, создан файл")

