from flask import  Flask
from Page import  Page

app = Flask(__name__)
pagina = Page('Ciao Simple Page Flask', 'Ciao, isso é uma pagina simples em Flask')

@app.route('/')
def hello():
    return pagina.imprimi

#  comando para começar aplicação
app.run()