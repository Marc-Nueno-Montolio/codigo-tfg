import_variables

% Configure Window
plannerWindow = figure('Name', 'Planificador RRT*', 'NumberTitle','off');
disp('Planning using RRT* Planner')

% Convert to binary Occupancy Map
binMap = to_binary_occupancy_map(myOccMap);

% Inflate the map to avoid collisions
robotRadius = 0.02;
inflatedMap = copy(binMap);
inflate(inflatedMap,robotRadius)
show(inflatedMap);

% Create validator
ss = stateSpaceSE2;
ss.StateBounds = [inflatedMap.XWorldLimits;inflatedMap.YWorldLimits;[-pi pi]];sv = validatorOccupancyMap(ss);
sv.Map = inflatedMap;

% Initialise planner
planner = plannerRRTStar(ss,sv, ContinueAfterGoalReached=true, MaxIterations=2500, ...
    MaxConnectionDistance=0.3);

% Plan path
start = [0.5 0.5 0];
goal = [-4 4 0];

[pthObj,solnInfo] = plan(planner,start,goal);

show(binMap)
hold on
% Tree expansion
plot(solnInfo.TreeData(:,1),solnInfo.TreeData(:,2),'.-')
% Draw path
plot(pthObj.States(:,1),pthObj.States(:,2),'r-','LineWidth',2)
drawnow
