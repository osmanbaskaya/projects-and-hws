function [model] = fitFn(Xtrain, ytrain,K)
% given training data and a regularization term, returns
% a model
i_theta = zeros(length(Xtrain(1,:)),1);
%[a,b] = costFunctionReg(i_theta,X,y)
options = optimset('GradObj', 'on', 'MaxIter', 400);
[theta, cost, i] = fminunc(@(t)(costFunctionReg(t, Xtrain, ytrain, K)), i_theta, options);
model = theta;
if i < 1
    display('convergence problem!!!!');
end
