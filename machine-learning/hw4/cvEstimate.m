function [mu, se] = cvEstimate(fitFn, X, y, K,  Nfolds, varargin)
% Cross validation estimate of expected loss
% model = fitFn(Xtrain, ytrain,K)
% X is N*D design matrix
% y is N*1
% Nfolds is number of CV folds
% Alternatively, you can explicitly specify the test folds
% using testFolds(:,f) for the f'th fold
% 
% mu is empirical estimate of expected loss
% se is standard error of this estimate

% This file is from matlabtools.googlecode.com


[testFolds, randomizeOrder] = process_options(varargin, ...
  'testFolds', [], 'randomizeOrder', true);

N = size(X,1);
if isempty(testFolds)
  [trainfolds, testfolds] = Kfold(N, Nfolds, randomizeOrder);
else
  % explicitly specify the test folds
  [nTest nFolds] = size(testFolds);
  testfolds = mat2cell(testFolds, nTest, ones(nFolds,1));
  trainfolds = cellfun(@(t)setdiff(1:N,t), testfolds, 'UniformOutput', false);
end
loss = zeros(1,N);
for f=1:length(trainfolds)
   Xtrain = X(trainfolds{f},:); Xtest = X(testfolds{f},:);
   ytrain = y(trainfolds{f}); ytest = y(testfolds{f});
   model = fitFn(Xtrain, ytrain,K);
   yhat = logregPredict(model, Xtest);
   loss(testfolds{f}) = double(yhat == ytest);
end 
mu = mean(loss);
se = std(loss)/sqrt(N);

end
