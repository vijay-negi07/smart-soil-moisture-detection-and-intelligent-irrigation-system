import os

for cls in ['dry', 'normal', 'wet']:
    path = os.path.join('dataset', cls)
    print(cls, ":", len(os.listdir(path)))
