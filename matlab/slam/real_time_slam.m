function slamAlg = real_time_slam
    % Crear suscripciones a los temas
    scanSub = rossubscriber('/scan','DataFormat','struct');
    odomSub = rossubscriber('/odom','DataFormat','struct');
    
    
    % Parámetros del algoritmo SLAM
    maxLidarRange = 8;
    mapResolution = 40;
    slamAlg = lidarSLAM(mapResolution, maxLidarRange);
    slamAlg.LoopClosureThreshold = 70;  
    slamAlg.LoopClosureSearchRadius = 1;
    
    
    f = uifigure('Name', 'Algoritmo SLAM tiempo real');
    b = uibutton(f,'Text','Finalizar'); 
    ax = uiaxes(f, "GridLineStyle","--");
    f.Position = [100 100 640 480];
    ax.Position = [1 1 640 438];
    ax.XGrid = 'on'
    ax.YGrid = 'on'
    ax.XLim = [-4, 4]
    ax.YLim = [-4, 4]

    b.Position = [531 446 100 23];

    
   
    
    
    keepRunning = true;
    
    b.ButtonPushedFcn = @(~,~) stopButtonPushed();
    function stopButtonPushed()
        keepRunning = false;
    end
    
    
    while keepRunning
        scanMessage = receive(scanSub); 
        scan = rosReadLidarScan(scanMessage);
        % Rotate scan
        scan = transformScan(scan, [0,0, -pi/2])
        addScan(slamAlg, scan);
        show(slamAlg, "Parent", ax);
        drawnow
        
    end

    save('./workspace/slam','slamAlg')

end
