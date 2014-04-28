function [model] = fitFn(Xtrain, ytrain,K)
% you should implement ridge regression here

Xnew = [ones(length(Xtrain), 1), Xtrain];
[~, n] = size(Xnew);
model = inv(K * eye(n) + Xnew' * Xnew) * Xnew' * ytrain;


end