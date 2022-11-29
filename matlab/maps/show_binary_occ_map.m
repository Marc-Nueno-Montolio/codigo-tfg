bin_map = load('./workspace/bin_occ_map.mat').map
f = figure('Name', 'Mapa de Ocupación Binaria', 'NumberTitle','off');
show(bin_map)
drawnow