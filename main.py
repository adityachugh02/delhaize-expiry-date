from utils.ocr import Ocr
from utils.formatting import formatting
from flask import Flask, flash, request, Response, render_template, redirect
from flask_cors import CORS
import base64
from PIL import Image
from io import BytesIO
import os

ocr = Ocr()

app = Flask(__name__)
CORS(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

result = ""

@app.route('/', methods= ["GET"])
def index():
    return render_template('index.html', result=result)

@app.route('/app.js', methods= ["GET"])
def js():
    return app.send_static_file('app.js')

@app.route('/style.css', methods= ["GET"])
def css():
    return app.send_static_file('style.css')


@app.route('/', methods= ["POST"])
def recognize():
    if 'image' in request.form:
        dataURL = request.form['image']
        dataURL = dataURL.split(",")
        dataURL = dataURL[1]
        dataURL = bytes(dataURL, 'utf-8')

        with open("temp.jpg", "wb") as fh:
            fh.write(base64.decodebytes(dataURL))

        im = Image.open("temp.jpg")
        width, height = im.size
        left = 2 * width / 6
        top = 7 * height / 16
        right = 4 * width / 6
        bottom = 9 * height / 16

        image = im.crop((left, top, right, bottom))
        image.save("temp.jpg")
        #im1.show()

        text_string = ocr.ocr("temp.jpg")
        global result
        result = formatting(text_string)
        print(result)
        return render_template('index.html')
    
    elif 'image' in request.files:
        image = request.files['image']
        image.save("temp.jpg")
        text_string = ocr.ocr("temp.jpg")
        print(text_string)
        result = formatting(text_string)
        print(result)
        return {
        "prediction": result,
    }

    else:
        return Response(status=400)
    

if __name__ == '__main__':
    # You want to put the value of the env variable PORT if it exist (some services only open specifiques ports)
    port = int(os.environ.get('PORT', 5000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)
