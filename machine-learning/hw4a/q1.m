clear;
load('spamData.mat');
Xtrain1a = [ones(length(Xtrain),1) convert1a(Xtrain)];
Xtest1a = [ones(length(Xtest),1) convert1a(Xtest)];

Xtrain1b = [ones(length(Xtrain),1) log(Xtrain+0.1)];
Xtest1b = [ones(length(Xtest),1) log(Xtest+0.1)];

Xtrain1c = [ones(length(Xtrain),1) Xtrain>0];
Xtest1c = [ones(length(Xtest),1) Xtest>0];

%fitFn(Xtrain1a,ytrain,3);
Ks = [logspace(1,0,20) 0];

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1a,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1a);
err = 1 - length(find(corrects))/length(corrects)
fprintf('stdn:\ttraining:%.3f test:%.3f\n',1-mean(mu),err);

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1b,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1b);
err = 1 - length(find(corrects))/length(corrects)
fprintf('log:\ttraining:%.3f test:%.3f\n',1-mean(mu),err);

[w, Kstar, mu, se] = fitCv(Ks, Xtrain1c,ytrain,5);
corrects = ytest == logregPredict(w,Xtest1c);
err = 1 - length(find(corrects))/length(corrects)
fprintf('binary:\ttraining:%.3f test:%.3f\n',1-mean(mu),err);