clear all;
load spamData
Ks = [1, 2, 4, 8];
[m, ~] = size(Xtrain);
%% Feature Normalization (for training)

[Xtrain, mu, sigma] = featureNormalize(Xtrain);
Xtrain =  [ones(m, 1) Xtrain]; % Adding X_zero feature
%% Normalize the test data with the same sigma and mu

Xtest = bsxfun(@minus, Xtest, mu);
Xtest = bsxfun(@rdivide, Xtest, sigma);

[m, ~] = size(Xtest);
Xtest =  [ones(m, 1) Xtest]; % Adding X_zero feature

[model, Kstar, mu, se] = fitCv(Ks, Xtrain, ytrain,  5); 