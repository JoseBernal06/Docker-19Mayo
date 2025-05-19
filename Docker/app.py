
from flask import Flask

servidorUno = Flask(__name__)

@servidorUno.route('/')
def hola():
    return "Hola mundo"


if __name__ == '__main__':
    servidorUno.run(host='0.0.0.0', port=5002)

