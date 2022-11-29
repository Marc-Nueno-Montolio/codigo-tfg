[goalPub, msg] = rospublisher("/move_base/goal","DataFormat","struct");

goal = [1.77 3.68]

msg.Goal.TargetPose.Header.FrameId = 'map'
msg.GoalId.Id =  'Primer Goal'
msg.Goal.TargetPose.Pose.Position.X = goal(2)
msg.Goal.TargetPose.Pose.Position.Y = - goal(1)
msg.Goal.TargetPose.Pose.Orientation.W = 1

send(goalPub, msg)

