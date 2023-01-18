function [] = video_detector
    warning('off','all')
    % Crear suscripciones a los temas
    camSub = rossubscriber('/usb_cam/image_raw');
    
    f = uifigure('Name', 'Registro de inventario: Posicione el AGV delante de la mercancía');
    b = uibutton(f,'Text','Finalizar'); 
    ax = uiaxes(f, "GridLineStyle","--");
    f.Position = [100 100 640 480];
    ax.Position = [1 1 640 438];

    b.Position = [531 446 100 23];
   
    keepRunning = true;
    
    b.ButtonPushedFcn = @(~,~) stopButtonPushed();
    function stopButtonPushed()
        keepRunning = false;
    end
    
    
    while keepRunning
        msg = receive(camSub);
        img = rosReadImage(struct(msg));
        I = detect_tag(img);
        imshow(I, "Parent",ax);

        drawnow;
        
    end


end
