import socketio

# Create a SocketIO instance
sio = socketio.Client()

# Connect to the server
sio.connect('http://localhost:8888')

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('response')
def on_response(data):
    response = data['response']
    print('Received response:', response)

while True:
    message = input("Enter a message to send: ")
    sio.emit('send_message', {'message': message})

# To close the connection gracefully when done
sio.disconnect()