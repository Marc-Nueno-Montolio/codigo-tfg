global slamAlgRunning;

slamAlgRunning = false;

disp('AGV MATLAB backend')
port = input('TCP Server port: ');
server = servidorTCP(port);

