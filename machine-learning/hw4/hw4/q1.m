clear all; clc;
load('spamData.mat');

%% data 1
Xtrain1a = [ones(length(Xtrain),1) convert1a(Xtrain)];
Xtest1a = [ones(length(Xtest),1) convert1a(Xtest)];

%% data 2
Xtrain1b = [ones(length(Xtrain),1) log(Xtrain+0.1)];
Xtest1b = [ones(length(Xtest),1) log(Xtest+0.1)];

%% data 3
Xtrain1c = [ones(length(Xtrain),1) Xtrain>0];
Xtest1c = [ones(length(Xtest),1) Xtest>0];

Ks = [logspace(1,0,20) 0];

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1a,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1a);
err = 1 - length(find(corrects))/length(corrects)
fprintf('std:\tTraining:%.3f Test:%.3f\n',1-mean(mu),err);

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1b,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1b);
err = 1 - length(find(corrects))/length(corrects)
fprintf('Log:\tTraining:%.3f Test:%.3f\n',1-mean(mu),err);

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1c,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1c);
err = 1 - length(find(corrects))/length(corrects)
fprintf('Binary:\tTraining:%.3f Test:%.3f\n',1-mean(mu),err);
