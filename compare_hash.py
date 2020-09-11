import requests
import urllib.request
import hashlib
import time
from bs4 import BeautifulSoup
import html2text
import difflib
import save 
import index
response = save.save_response()
oldhash= save.save_oldhash()
newresponse1= urllib.request.urlopen('file:///C:/Users/KrizelDias/Downloads/html/TMPH00033/index.html').read()
newhash = hashlib.sha224(newresponse1).hexdigest()
index.create_html_file()

if(oldhash==newhash):
    html_str = """
    <div class="bg">
    <div class="layer">
    <div class="header_text">
    <h1 style="color:blue;">Welcome to WebSite Update Tracker<h1>
    <h2>Webpage was not updated</h2>
    </div>
    </div>
    </div>
    </body>"""
    Html_file= open("index.html","a")
    Html_file.write(html_str)
    Html_file.close()
else:
    html_str = """
    <div class="bg">
    <div class="layer">
    <div class="header_text">
    <h1 style="color:blue;font-size:300%;">Welcome to WebSite Update Tracker<h1>
    <h2 style="font-size:200%;color:red;">WebSite was updated</h2>
    <h2 style="font-size:180%;">Contents changed</h2>
    </div>"""
    Html_file= open("index.html","a")
    Html_file.write(html_str)
    newresponse = newresponse1.decode("utf-8", "ignore")
    newresponse = html2text.html2text(newresponse)
    diff= difflib.SequenceMatcher(None,response,newresponse)
    result = ""
    for tag, i1, i2, j1, j2 in diff.get_opcodes():
        if(tag == "insert" or tag == "replace"):
                    result = newresponse[j1:j2+1]
                    if(tag=="insert"):
                        contents="New contents added on the WebSite = '{}'".format(result)
                        html_str = f"""
                        <div class="header_text">
                        <h3 style="font-family:courier;">{contents}</h3>
                        </div>
                        """
                        Html_file.write(html_str)
                    else:
                        contents="Contents {}d on the WebSite in place of '{}' = '{}'".format(tag,response[i1:i2+1],result)
                        html_str = f"""
                        <div class="header_text">
                        <h3 style="font-family:courier;">{contents}</h3>
                        </div>
                        """
                        Html_file.write(html_str)
                        
    html_str = """
    </div>
    </div>
    </body>"""
    Html_file.write(html_str)
    Html_file.close()


    
    
    
    
    
    
    
    
   
