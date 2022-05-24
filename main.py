from utils.ocr import Ocr
from utils.formatting import formatting
from flask import Flask

ocr_instance = Ocr()

app = Flask(__name__)

@app.route('/', methods= ["POST"])
def status():
    return 'alive'

@app.route('/', methods= ["GET"])
def recognize():
    text_string = ocr_instance.ocr("sample1.jpg")
    result = formatting(text_string)
    return result

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
