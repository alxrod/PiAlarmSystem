from flask import Flask
from flask import render_template
from flask import redirect
import os, glob

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/images')
def render_images():
    images = []
    for image in os.listdir("./static/images"):
        images.append(image)
    images.reverse()
    
    mostRecent = 0
    name = images[0]
    for image in images:
        time = int(image.split(".")[0])
        if time > mostRecent:
            name = image,
            mostRecent = time
    print "Final: " + str(name[0])
    return render_template('images.html', image=name[0])
    
@app.route('/calibrate', methods=['POST'])
def calibrate():
    print "Calibrating"
    with open("./sensor_status.txt", "r") as fp:
#         print fp.read()
        values = fp.read().split(",")
        print values
        values[1] = "True"
#         values = ["0","False","False"]
        values = ",".join(values)
    with open("./sensor_status.txt", "w") as fp:
        fp.write(values)
        fp.close()
    return redirect("/images")

@app.route('/collect', methods=['POST'])
def collect():
    print "Collecting!"
    with open("./sensor_status.txt", "r") as fp:
#         print fp.read()
        values = fp.read().split(",")
        print values
        values[2] = "True"
#         values = ["0","False","False"]
        values = ",".join(values)
    with open("./sensor_status.txt", "w") as fp:
        fp.write(values)
        fp.close()
    return redirect("/images")