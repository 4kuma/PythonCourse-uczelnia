import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        src = os.path.realpath(name)
        if root[2:] == '':
            print(src[:-(len(name))] + root[2:] + name)
            os.rename(src[:-(len(name))] + root[2:] + name, src[:-(len(name))] + root[2:] + name.lower())
        else:
            os.rename(src[:-(len(name))] + root[2:] +'\\' + name, src[:-(len(name))] + root[2:] +'\\' + name.lower())
    for name in dirs:
        src = os.path.realpath(name)
        if root[2:] == '':
            print(src[:-(len(name))] + root[2:] + name)
            os.rename(src[:-(len(name))] + root[2:] + name, src[:-(len(name))] + root[2:] + name.lower())
        else:
            os.rename(src[:-(len(name))] + root[2:] + '\\' + name, src[:-(len(name))] + root[2:] + '\\' + name.lower())