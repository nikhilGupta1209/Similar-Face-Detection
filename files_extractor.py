import os
import pickle

files = os.listdir('data')


filesname = []

for file in files:
    for actor in os.listdir(os.path.join('data', file)):
        # print(os.path.join('data', file, actor))
        for photo in os.listdir(os.path.join('data', file, actor)):
            filesname.append(os.path.join('data', file, actor, photo))



# print(len(filesname))
pickle.dump(filesname, open('actorsname.pkl', 'wb'))