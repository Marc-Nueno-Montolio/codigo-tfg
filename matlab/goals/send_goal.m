function result = send_goal(identifier, goal, orientation)

    [goalPub, goalMsg] = rospublisher("/move_base/goal","DataFormat","struct");
    goalStatusSub = rossubscriber('/move_base/status','DataFormat','struct');
    
    %goal = [1.77 3.68];
    %id = 'goal_test';


    if ~exist('orientation','var')
        goalMsg.Goal.TargetPose.Pose.Orientation.W = 1;
    else
        goalMsg.Goal.TargetPose.Pose.Orientation = orientation;
    end
    
    goal_id = [identifier '_' char(randi([48 90],1,10))]
    
    goalMsg.Goal.TargetPose.Header.FrameId = 'map';
    goalMsg.GoalId.Id =  goal_id;
    goalMsg.Goal.TargetPose.Pose.Position.X =  goal(2);
    goalMsg.Goal.TargetPose.Pose.Position.Y = - goal(1);
    
    
    send(goalPub, goalMsg);
    pause(0.5)
    
    goal_status = currentGoalStatus(goal_id, goalStatusSub);
    status = goal_status.StatusList.Status;
    
    if status == 3
        disp('Goal Reached');
        result = 'ok';
    else
    
        while status ~= 3
            disp('Working ...')
            goal_status = currentGoalStatus(goal_id, goalStatusSub);
            status = goal_status.StatusList.Status;
            pause(1)
    
            if status == 4
                disp('Failed to reach goal')
                result = 'ko';
                break
            end
            
        end
        disp('Goal Reached');
        result = 'ok';
    end
    
    
    
    function goalStatus = currentGoalStatus(goal_id, goalStatusSub)
    
        msg = receive(goalStatusSub);
        id = msg.StatusList.GoalId;
        id = id.Id;
    
        while (strcmp(id,goal_id) ~= true)
            msg = receive(goalStatusSub);
            id = msg.StatusList.GoalId;
            id = id.Id;
        end
        goalStatus = msg;
    
    end
end

