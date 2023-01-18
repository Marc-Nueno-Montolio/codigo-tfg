amclSub = rossubscriber('/amcl_pose','DataFormat','struct');

msg = receive(amclSub, 5);

%real_pos = [msg.Pose.Pose.Position.X msg.Pose.Pose.Position.Y,msg.Pose.Pose.Position.Z]
estimated_pos = [-msg.Pose.Pose.Position.Y msg.Pose.Pose.Position.X,msg.Pose.Pose.Position.Z]
estimated_orientation = [ msg.Pose.Pose.Orientation.X  msg.Pose.Pose.Orientation.Y  msg.Pose.Pose.Orientation.Z  msg.Pose.Pose.Orientation.W]
orientation = msg.Pose.Pose.Orientation;
origin = pos;
clear amclSub