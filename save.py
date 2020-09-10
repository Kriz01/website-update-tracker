import oldpage
import pickle 
def save_response():
    file = open('response', 'rb')
    response = pickle.load(file)
    file.close()
    return response
    
def save_oldhash():
    file = open('oldhash', 'rb')
    oldhash = pickle.load(file)
    file.close()
    return oldhash
