from urllib import request
from urllib.error import URLError

def wordsFile(url):
    try:
        file = request.urlopen(url)
    except URLError:
        return("¡La url " + url + " no existe!")
    else:
        content = file.read()
        return len(content.split())

print(wordsFile("https://www.gutenberg.org/files/2000/2000-0.txt"))
print(wordsFile("https://no-existe.txt"))