binMap = load('./workspace/bin_occ_map.mat').map;
plannerWindow = figure('Name', 'Planificador PRM', 'NumberTitle','off');

disp('Updating PRM Planner')
% Inflate the map to avoid collisions
robotRadius = 0.02;
inflatedMap = copy(binMap);
inflate(inflatedMap,robotRadius)

show(inflatedMap);

prm = mobileRobotPRM(inflatedMap, 50)
prm.ConnectionDistance = 6;

save('./workspace/planners/prm','prm')
show(prm)
drawnow
