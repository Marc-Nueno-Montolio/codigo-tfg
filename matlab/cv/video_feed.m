function [img] = video_feed
    % Crear suscripciones a los temas
    camSub = rossubscriber('/usb_cam/image_raw');
   
    
    f = uifigure('Name', 'Vídeo en tiempo real');
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
        imshow(img, "Parent",ax);
        drawnow;
        
    end


end












