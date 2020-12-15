import os
result = []


def countWebsites(name):
    return


def walkDir(working_dir):
    # walk through all the files/directories
    for root, dirs, files in os.walk(working_dir):
        for name in files:
            name_split = os.path.splitext(name)
            f_name, f_type = name_split
            # only csv files are taken into consideration
            if f_type == '.csv':
                print(name)
                countWebsites(name)


walkDir('.')
