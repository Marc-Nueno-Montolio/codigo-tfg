import json,socket, base64

class MatlabClient():
    def __init__(self, port):
        self.host = '127.0.0.1'
        self.port = 5050
        self.s = socket.socket()
        print(f"Created Socket on {self.host}:{self.port}")
        
    def connect(self):
        # Connect to MATLAB TCP Server
        try:
            self.s.connect((self.host, self.port))
            print('Connected!')
        except:
            print('Problem Connecting')

    def disconnect(self):
        try:
            self.s.close()
            print('Disonnected!')
        except:
            print('Problem Disconnecting')

    def send_command(self, command, args):
        payload = {
            "command": command,
            "args": args}

        # Convert Command to JSON
        json_data = json.dumps(payload)

        # encode json as utf-8
        self.s.sendall(bytes(json_data,encoding="utf-8"))


