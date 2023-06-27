from flask import Flask,request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
import time
import gevent

 
app = Flask(__name__) 
@app.route("/dyconn")
def dyconn():
    user_socket = request.environ
    myObject.ws = user_socket
    websocket_obj = user_socket['wsgi.websocket']
    while True:  
        msg = websocket_obj.receive()
        #print(msg)
        myObject.sign = msg
        print("[info] sign change at"+str(time.time()))

@app.route("/dysign", methods=['GET'])
def dy():
    data = request.args.get('data')
    if myObject.ws is  None:
        return '[Error] WebSocket connection does not exist.'
    else:
        try:
            websocket_obj = myObject.ws['wsgi.websocket']
            print("[+] Websocket Sever Connect Success.")
        except:
            return '[Error] WebSocket connection does not exist.'
    websocket_obj.send(data)
    print("[info] msg send at"+str(time.time()))
    #print("[*] " + data + " has been sent to client. ^^")
    gevent.sleep(0.05)
    print("[info] Response at"+str(time.time()))
    return myObject.sign

class MyCONN:
    ws = None,
    sign = "depysign"

if __name__ == '__main__':
    myObject = MyCONN()
    http_serv = WSGIServer(("0.0.0.0",9432),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
