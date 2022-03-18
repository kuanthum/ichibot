import urllib.request, urllib.parse, urllib.error, operator

try:
    url = 'https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt'
    url_data = urllib.request.urlopen(url)
    count = dict()
    for line in url_data:
        #lista
        nombres = line.decode().split()
        print(nombres)
        for nombre in nombres:
            count[nombre[0]] = count.get(nombre[0]) + 1
    print(count)
    pass
except Exception as err:
    print("Error", err)