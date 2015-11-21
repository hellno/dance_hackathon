%% script plot
% simple script to plot incoming data in log.csv
% data are classes arranged by python script
load('log.csv')
length = size(log);
x = 1:length;
plot(x, log)