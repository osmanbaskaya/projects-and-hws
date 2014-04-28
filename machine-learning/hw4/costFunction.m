function [J, grad] = costFunction(t, X, y, lambda)

m = length(y);
J = 0;
grad = zeros(size(t));

Z = sigmoid(X * t);

J = ((-y .* log(Z)) - ((1-y) .* log(1 - Z))) / m;

regJ = lambda * (t(2:end)' * t(2:end)) / (2*m);

J = sum(J) + regJ;

grad(1) = (Z-y)' * X(:,1) / m;
grad(2:end) = ((Z-y)' * X(:,2:end) / m) + (lambda * t(2:end))' / m;



%grad(1) = (1/m) * sum( ((X * theta) - y) .* X(:,1) );
%grad(2:end) = (((1/m) * ((X * theta) - y)' * X(:,2:end)))' + (lambda/m)*theta(2:end);


end
