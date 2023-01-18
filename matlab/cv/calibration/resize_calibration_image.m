filename = "./workspace/cv/calibration/checker_x.png"
sizes = [480, 640];
original = imread(filename);
output = imresize(original,sizes);
imwrite(output,filename);
