function [J, grad] = costFunctionReg(theta, X, y, lambda)
hx = sigmoid(X * theta);
m = length(X);

J = (sum(-y' * log(hx) - (1 - y')*log(1 - hx)) / m) + lambda * sum(theta(2:end).^2) / (2*m);
grad =((hx - y)' * X / m)' + lambda .* theta .* [0; ones(length(theta)-1, 1)] ./ m ;

end