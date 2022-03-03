import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2
 
# CONNECT FIX ==> conda install -c conda-forge python-engineio=3.0.0

i = 0
sio = socketio.Server()
 
app = Flask(__name__) #'__main__'
speed_limit = 10

def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    #img = img/255
    return img
 
# escucha el evento telemetry 
@sio.on('telemetry')
def telemetry(sid, data):
    global i
    speed = float(data['speed'])
    
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = img_preprocess(np.asarray(image))

    cv2.imwrite("img/"+ str(i) + ".png", image)
    i = i + 1

    image = np.array([image])

    # PREDECIR CON EL MODELO
    steering_angle = float(model.predict(image))
    
    # AJUSTE ACELERACION
    throttle = 1.0 - speed/speed_limit
    
    print('manivela:{} aceleracion:{} velocidad:{}'.format(steering_angle, throttle, speed))
    
    # Emite datos hacia el cliente (emit-socket)
    send_control(steering_angle, throttle)
 
@sio.on('connect')
def connect(sid, environ):
    # primera conexion recibida del socket
    print('Connected')
    send_control(0, 0)
 
def send_control(steering_angle, throttle):
    # Envia JSON (emit) via socket
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })
 
if __name__ == '__main__':
    model = load_model('model.h5') # modelo generado en el notebook
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)