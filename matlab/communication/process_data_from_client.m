function [] = process_data(data)
    command = data.command;
    args = data.args;
    disp(strcat("Comando", ": ", command))

    if command == "show_occ_map"
        show_binary_occ_map
    elseif command == "generate-slam"
        global slamAlgRunning;

        if slamAlgRunning == true
            slamAlgRunning = false;
        else
            slamAlgRunning = true;
        end
        disp(slamAlgRunning)
        real_time_slam

    elseif command == "update_planner"
        PRM
    else
        disp('Comando no reconocido')
        disp(data)
    end
end

