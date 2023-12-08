f = open("downloadlist.txt")

raw = f.read()
split = raw.split('"')

filename = False
urls = []
for name in split:
    if filename:
        print(name)
    filename = not filename

