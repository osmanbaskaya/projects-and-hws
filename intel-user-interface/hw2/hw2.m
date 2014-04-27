clc; clear; close all;

addpath('libsvm-3.18/matlab/');
k = 5;

%% Read data
data = csvread('Input.txt');


%%  Shuffle the data
rng(0) % Seed = 0
ridx = randperm(length(data));
data = data(ridx, :); % Shuffling the data
data = data(1:150,:);

%% Run LibSVM with different kernels and parameters

%linearSVM_params = '-s 0 -t 0 -c %d -h 0 -g %d';
%linear_accuracies = run(data, k, linearSVM_params, 'Linear');

rbfSVM_params = '-s 0 -t 2 -c %d -h 0 -g %d';
rbf_accuracies = run(data, k, rbfSVM_params, 'RBF');

%polySVM_params = '-s 0 -t 1 -c %d -h 0 -g %d';
%poly_accuracies = run(data, k, polySVM_params, 'Polynomial');
x = 1;