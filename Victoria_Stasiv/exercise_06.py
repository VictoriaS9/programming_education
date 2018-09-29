import random


def txt_handler(filename):
    if filename.endswith('txt'):
        r = random.randint(100, 450)
        print(r)
        return 'txt'


def zip_handler(filename):
    if filename.endswith('zip'):
        r2 = random.randint(500, 700)
        print(r2)
        return 'zip'


def jpg_handler(filename):
    if filename.endswith('jpg'):
        r3 = random.randint(800, 1000)
        print(r3)
        return 'jpg'


def ttf_handler(filename):
    if filename.endswith('ttf'):
        r4 = random.randint(1000, 2000)
        print(r4)
        return 'ttf'


def ini_handler(filename):
    if filename.endswith('ini'):
        r5 = random.randint(1500, 1700)
        print(r5)
        return 'ini'


def recognize_file_type(filename):
    if filename.endswith('txt'):
        txt_handler(filename)
        return 'txt'
    elif filename.endswith('zip'):
        zip_handler(filename)
        return 'zip'
    elif filename.endswith('jpg'):
        jpg_handler(filename)
        return 'jpg'
    elif filename.endswith('ttf'):
        ttf_handler(filename)
        return 'ttf'
    elif filename.endswith('ini'):
        ini_handler(filename)
        return 'ini'
print(recognize_file_type("file.txt"))

list_of_files = ["reports.txt", "monthly_reports.zip", "README.txt", "picture.jog", "logo.ttf", "config.ini"]
def run_executors(list_of_files):
    for i in list_of_files:
       print(recognize_file_type(i))


run_executors(list_of_files)
