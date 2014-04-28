clear, clc;
load('spamData.mat');

%% Binarized the data

XtrainB = Xtrain>0;
XtestB = Xtest>0;


%% Add one smoothing (question a)

Xtrain_add1 = XtrainB + 1;
Xtest_add1 = XtestB + 1;

%% Parameter Estimation

[prior0, prior1, cond0, cond1] = NaiveBayesParameterEst(Xtrain_add1, ytrain);


















% Xtrain1c = Xtrain>0;
% Xtest1c = Xtest>0;
% 
% py_1 = find(ytrain)/length(ytrain);
% py_0 = 1-py_1;
% 
% total = sum(Xtrain1c);
% birler = sum(Xtrain1c(find(ytrain),:)) + 1;
% sifirlar = total - birler;
% birler = birler + 1;
% sifirlar = sifirlar + 1;
% total = birler + sifirlar;