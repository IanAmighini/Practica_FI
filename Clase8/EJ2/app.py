#A
#1 /productos/     GET
#2 /productos/<int:id>/    GET
#3 /productos/  PUT
#4 /productos/ DELETE

from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

dic = {'Producto':['Shampoo Solido', 'Crema de manos'], 'Stock':[5,6], 'Precio_unitario':[300,600]}
df = pd.DataFrame(dic)
df.index += 1

df.html = df.to_html()

@app.get('/')
def home():
    return render_template('home_cosmetics.html')

@app.get('/productos/')
def get_productos():
    return render_template('cosmetics.html')

@app.get('/productos/<int:indice>/')
def get_producto(indice):
    if indice in df.index:
        producto = producto[indice]
        return render_template('producto.html', indice=indice, producto=producto)
    else:
        return ("no existe ese producto", 404)