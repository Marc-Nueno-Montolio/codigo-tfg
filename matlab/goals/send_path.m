function [] = send_path(path)

    for i = 1 : length(path)
        disp(['Sending ' 'goal_' sprintf('%d', i)])
        result = send_goal(['goal_' i], path(i, :));
    end

end
