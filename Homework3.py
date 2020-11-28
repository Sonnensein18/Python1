import os

f = r"C:\python"


def get_size(start_path='.'):
    size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
    return size


print(str(get_size(f)))
