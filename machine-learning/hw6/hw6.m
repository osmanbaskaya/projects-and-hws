clc, clear;

images = loadMNISTImages('train-images.idx3-ubyte');
labels = loadMNISTLabels('train-labels.idx1-ubyte');
 
visibleSize = 28*28;
hiddenSize = 196;
sparsityParam = 0.1;
lambda = 3e-3;
beta = 3;

numpatches = 10000;
patches = images(:, 1:numpatches);
patches0 = images(:, 1:3);

theta = initializeParameters(hiddenSize, visibleSize);
[cost, grad] = sparseAutoencoderCost(theta, visibleSize, hiddenSize, lambda, ...
                                     sparsityParam, beta, patches0);
disp('grad');
disp(size(grad));
%%======================================================================
%% STEP 3: Gradient Checking
%
% Hint: If you are debugging your code, performing gradient checking on smaller models 
% and smaller training sets (e.g., using only 10 training examples and 1-2 hidden 
% units) may speed things up.

% First, lets make sure your numerical gradient computation is correct for a
% simple function.  After you have implemented computeNumericalGradient.m,
% run the following: 
%checkNumericalGradient();


% Now we can use it to check your cost function and derivative calculations
% for the sparse autoencoder.  
%numgrad = computeNumericalGradient( @(x) sparseAutoencoderCost(x, visibleSize, ...
%                                                  hiddenSize, lambda, ...
 %                                                 sparsityParam, beta, ...
  %                                                patches0), theta);

% Use this to visually compare the gradients side by side
%disp([numgrad grad]); 

% Compare numerically computed gradients with the ones obtained from backpropagation
%diff = norm(numgrad-grad)/norm(numgrad+grad);
%disp(diff); % Should be small. In our implementation, these values are
            % usually less than 1e-9.

            % When you got this working, Congratulations!!!

%% 
%  Randomly initialize the parameters
theta = initializeParameters(hiddenSize, visibleSize);

%  Use minFunc to minimize the function
addpath minFunc/
options.Method = 'lbfgs'; % Here, we use L-BFGS to optimize our cost
                          % function. Generally, for minFunc to work, you
                          % need a function pointer with two outputs: the
                          % function value and the gradient. In our problem,
                          % sparseAutoencoderCost.m satisfies this.
options.maxIter = 400;	  % Maximum number of iterations of L-BFGS to run 
options.display = 'on';


[opttheta, cost] = minFunc( @(p) sparseAutoencoderCost(p, ...
                                   visibleSize, hiddenSize, ...
                                   lambda, sparsityParam, ...
                                   beta, patches), ...
                              theta, options);

%%======================================================================
%% STEP 5: Visualization 

W1 = reshape(opttheta(1:hiddenSize*visibleSize), hiddenSize, visibleSize);
display_network(W1', 12); 

print -djpeg weights.jpg   % save the visualization to a file 


