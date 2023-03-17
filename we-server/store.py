import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categorias = r.json()
    print(categorias)
    print(type(categorias))
    for category in categorias:
        print(category['name'])
