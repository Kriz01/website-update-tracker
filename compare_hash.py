import requests
import urllib.request
import hashlib
import time
from bs4 import BeautifulSoup
import html2text
import difflib
import save 
response = save.save_response()
oldhash= save.save_oldhash()
newresponse1= urllib.request.urlopen('file:///C:/Users/KrizelDias/Desktop/test.html').read()
newhash = hashlib.sha224(newresponse1).hexdigest()
if(oldhash==newhash):
    print("webpage was not updated")
else:
    print("webpage was updated") 
    newresponse = newresponse1.decode("utf-8", "ignore")
    newresponse = html2text.html2text(newresponse)
    diff= difflib.SequenceMatcher(None,response,newresponse)
    result = ""
    count=0
    for tag, i1, i2, j1, j2 in diff.get_opcodes():
        count=count+1
        if(tag == "insert" or tag == "replace"):
                    result = newresponse[j1:j2+1]
                    if(tag=="insert"):
                        print("new contents that are {}ed on webpage at line location {} = {}".format(tag,count,result))
                    else:
                        print("new contents that are {}d on webpage in place of '{}' at line location {} = {}".format(tag,response[i1:i2+1],count,result))
                        
                        



    
    
    
    
    
    
    
    
    
    
    
    
    




