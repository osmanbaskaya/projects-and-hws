function [cost, grad] = softmaxCost(theta, numClasses, inputSize, lambda, data, labels)

% numClasses - the number of classes 
% inputSize - the size N of the input vector
% lambda - weight decay parameter
% data - the N x M input matrix, where each column data(:, i) corresponds to
%        a single test set
% labels - an M x 1 matrix containing the labels corresponding for the input data
%

% Unroll the parameters from theta
theta = reshape(theta, numClasses, inputSize);

numCases = size(data, 2);

groundTruth = full(sparse(labels, 1:numCases, 1));
cost = 0;

thetagrad = zeros(numClasses, inputSize);

%% ---------- YOUR CODE HERE --------------------------------------
%  Instructions: Compute the cost and gradient for softmax regression.
%                You need to compute thetagrad and cost.
%                The groundTruth matrix might come in handy.

M = exp(theta * data);
actual = bsxfun(@dot, M, groundTruth);
Z = sum(M);

[m,~] = size(labels);
model_cost = -(1/m) * sum(log(actual ./ Z));
weight_decay_cost = sum((lambda / 2) * theta(:) .^ 2);
cost = model_cost + weight_decay_cost; % regularization ;)

p = bsxfun(@rdivide, M, Z);
thetagrad = -(1/m) * data * (groundTruth - p)';
thetagrad = thetagrad' + (lambda * theta); % from regularization

% ------------------------------------------------------------------
% Unroll the gradient matrices into a vector for minFunc
grad = [thetagrad(:)];
end

