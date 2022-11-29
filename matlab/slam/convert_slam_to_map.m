function map = convert_slam_to_map(slamAlg, binary)
[scans, optimizedPoses]  = scansAndPoses(slamAlg);
    map = buildMap(scans, optimizedPoses, slamAlg.MapResolution, slamAlg.MaxLidarRange);
    if binary == true
        map = to_binary_occupancy_map(map)
        save('./workspace/bin_occ_map','map')
    else
        save('./workspace/occ_map','map')
    end
end

