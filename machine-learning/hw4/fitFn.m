function [theta] = fitFn(X, y, lambda)
% given training data and a regularization term, returns
% a model


[n, d] = size(X);
initial_theta = zeros(d, 1);
opt = optimset('GradObj', 'on', 'MaxIter', 400);

[theta, cost] =	fminunc(@(t)(costFunction(t, X, y, lambda)), initial_theta, opt);

end

