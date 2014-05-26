function p = logregPredict(model, X)
% predicts class labels given a model, for data X
% you should implement a sigmoid function inorder to predict class labels
hx = sigmoid(X * model);
p = hx>0.5;
end
