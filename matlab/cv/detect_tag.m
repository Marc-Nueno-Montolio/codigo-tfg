

function [I] = detect_tag(I)
warning('off','all')
    %I = imread("aprilTagsMulti.jpg");
    %I = imread('./workspace/cv/images/marker.png');
    
    % Load camera intrinsic parameters
    intrinsics = load('./workspace/cv/calibration/intrinsics').cameraParams;
    
    % Specify tag family to detect
    tagFamily = ["tag36h11"];
    
    %Specify tag size
    tagSize = 0.04;
    
    I = undistortImage(I,intrinsics,OutputView="same");
    
    [id,loc,pose,detectedFamily] = readAprilTag(I,"tag36h11",intrinsics,tagSize);
    
    for idx = 1:length(id)
            % Display the ID and tag family
            %disp("Detected Tag ID: " + id(idx));
     
            % Insert markers to indicate the locations
            markerRadius = 8;
            numCorners = size(loc,1);
            markerPosition = [loc(:,:,idx),repmat(markerRadius,numCorners,1)];
            I = insertShape(I,"FilledCircle",markerPosition,Color="red",Opacity=1);

            % Mirar que el tag esté centrado
            if(loc(1,1)) > 150 
                distance = loc(2,1)-loc(1,1);
                if distance >= 100
                    I = insertText(I,loc(4,:,1), sprintf("ID: %d, dist: %.2f", id(idx), distance));
                    I = insertShape(I,"line", [loc(1,:), loc(2,:)], Color="green");
                    disp('Detected Tag!')
                    update_tag_location(id(idx))
                    
                end
            end
    end

    
    
end


