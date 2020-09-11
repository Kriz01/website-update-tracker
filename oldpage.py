import urllib.request
import  html2text
import hashlib
import pickle 
def write_file():
    response1= urllib.request.urlopen('ENTER THE WEBSITE LINK YOU WANT TO MONITOR').read()
    response = response1.decode("utf-8", "ignore")
    response = html2text.html2text(response)
    oldhash = hashlib.sha224(response1).hexdigest()
    file = open('response', 'wb')
    pickle.dump(response, file)
    file.close()
    file = open('oldhash', 'wb')
    pickle.dump(oldhash, file)
    file.close()
