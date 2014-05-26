clear;
load('spamData.mat');
Xtrain1c = Xtrain>0;
Xtest1c = Xtest>0;

py_1 = find(ytrain)/length(ytrain);
py_0 = 1-py_1;

total = sum(Xtrain1c);
birler = sum(Xtrain1c(find(ytrain),:)) + 1;
sifirlar = total - birler;
birler = birler + 1;
sifirlar = sifirlar + 1;
total = birler + sifirlar;