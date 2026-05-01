import string
import secrets

urls_store = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))

def create_unique_short_code():
    while True:
        short_code = generate_short_code()
        
        if short_code not in urls_store:
            
            return short_code


def url_short(original_url, server_url):

    short_code = create_unique_short_code()
    

    urls_store[short_code] = {
        "original_url": original_url,
        "short_url": server_url + short_code
    }
    
    return urls_store[short_code]


def get_original_url(short_code):
    if short_code in urls_store:
        return urls_store[short_code]["original_url"]
    else:
        return False
    
def return_urls_store():
    return urls_store

    
        
       







