function [server] = servidorTCP(port)

% Created Server
    server = tcpserver('127.0.0.1',port,"ConnectionChangedFcn",@connectionFcn);
    
end


function connectionFcn(src, ~)
    %Client is connected
        if src.Connected
            disp("Client connected")
            %Read Write infinitly with connected client
            while true
                if src.NumBytesAvailable > 0
                    bytes = read(src,src.NumBytesAvailable,'string');
                    data = jsondecode(sprintf(bytes));
                    process_data_from_client(data)
                else
                    pause(0.5)
                end

            end
        end
    end
