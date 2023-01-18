

% Configure Window
plannerWindow = figure('Name', 'Planificador Hybrid A*Grid', 'NumberTitle','off');
disp('Planning using Hybrid A*Grid Planner')

% Convert to binary Occupancy Map
binMap = map;

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
planner = plannerHybridAStar(sv, MinTurningRadius=1, MotionPrimitiveLength=1);

% Plan path
startPose = [origin 0]; % [meters, meters, radians]
goalPose = [goal 0];

path = plan(planner,startPose,goalPose,SearchMode='exhaustive');     

show(planner)
drawnow
