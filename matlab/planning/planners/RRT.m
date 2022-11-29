import_variables

% Configure Window
plannerWindow = figure('Name', 'Planificador RRT', 'NumberTitle','off');
disp('Planning using RRT Planner')

% Convert to binary Occupancy Map
binMap = to_binary_occupancy_map(myOccMap);

% Inflate the map to avoid collisions
robotRadius = 0.02;
inflatedMap = copy(binMap);
inflate(inflatedMap,robotRadius)
show(inflatedMap);

% Create validator
ss = stateSpaceSE2;
sv = validatorOccupancyMap(ss);
sv.Map = inflatedMap;
sv.ValidationDistance = 0.01;
ss.StateBounds = [inflatedMap.XWorldLimits;inflatedMap.YWorldLimits;[-pi pi]];

% Initialise planner
planner = plannerRRT(ss,sv,MaxConnectionDistance=0.3);

% Plan path
start = [0.5 0.5 0];
goal = [-4 4 0];

rng(100,'twister'); % for repeatable result
[pthObj,solnInfo] = plan(planner,start,goal);

show(binMap)
hold on
% Tree expansion
plot(solnInfo.TreeData(:,1),solnInfo.TreeData(:,2),'.-')
% Draw path
plot(pthObj.States(:,1),pthObj.States(:,2),'r-','LineWidth',2)
hold off
drawnow
