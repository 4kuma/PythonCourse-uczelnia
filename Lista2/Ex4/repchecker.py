import os
import hashlib

dict = {}

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        file_path = os.path.realpath(name)[:-len(name)] + os.path.join(root, name)[1:]
        with open(file_path, 'r') as input_file:
            txt = input_file.read()
        if dict.get((os.path.getsize(file_path), hashlib.md5(txt.encode()).hexdigest())) == None:
            dict[(os.path.getsize(file_path), hashlib.md5(txt.encode()).hexdigest())] = [os.path.join(root, name)]
        else:
            dict[(os.path.getsize(file_path), hashlib.md5(txt.encode()).hexdigest())].append(os.path.join(root, name))

for key, item in dict.items():
    print('-----------------------------------------')
    for i in item:
        print(i)
