function path = path_from_prm(origin,goal)
    prm = load('./workspace/planners/prm').prm
    path = findpath(prm,origin,goal);
    show(prm)
    path = path(2:end, :)

    save('./workspace/planners/latest_path','path')
end

