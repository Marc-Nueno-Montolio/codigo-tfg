function [binOccupancyMap] = to_binary_occupancy_map(occupancyMap)
%   Converts a grayscale occupancy map to a binary occupancy map, to be
%   used by path planning algorithms.

% Convert map to matrix
map = occupancyMatrix(occupancyMap);

%Parse rows and columns
sz = size(map);
rows = sz(1,1);
columns = sz(1,2);

% Create Binary Map of the same size
binMap = zeros(rows,columns);

% Parse the occupancy map
for x = 1:rows
    for y = 1:columns
        if map(x,y) > 0.5
            binMap(x,y) = 1;
        end
    end
end

binOccupancyMap = binaryOccupancyMap( ...
    binMap, ...
    GridOriginInLocal=occupancyMap.GridOriginInLocal, ...
    LocalOriginInWorld=occupancyMap.LocalOriginInWorld, ...
    Resolution=occupancyMap.Resolution ...
    );
% Mantain original map properties:

end

