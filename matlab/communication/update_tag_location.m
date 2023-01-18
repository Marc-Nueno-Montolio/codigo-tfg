function [] = update_tag_location(id)
    odomSub = rossubscriber('/odom');
    msg = receive(odomSub);
    pos = [msg.Pose.Pose.Position.X -msg.Pose.Pose.Position.Y msg.Pose.Pose.Position.Z];

    % ToDo: HTTP POST to update position in db
    disp(sprintf("Tag %d position updated to %.2f %.2f %.2f", id, pos(1),pos(2),pos(3)))
    
end

