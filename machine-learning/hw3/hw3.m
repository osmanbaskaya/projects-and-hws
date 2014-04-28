clear
load prostate
%% Question 1
Xnew = [ones(length(Xtrain), 1), Xtrain];
w = inv(Xnew' * Xnew) * Xnew' * ytrain;
Xnew = [ones(length(Xtest), 1), Xtest];
y_hat = Xnew * w;
err = (ytest - y_hat);
se = err' * err;
mse = se / length(ytest);
stderr = std(err .* err) / sqrt(length(ytest));
fprintf('MSE: %f\n', mse); 
fprintf('Standard Error: %f\n', stderr);

%% Question 2
Ks = logspace(3, 0, 20);
[w, Kstar, mu, see] = fitCv(Ks, X, y, 5);
y_hat = Xnew * w;
err = (ytest - y_hat);
se = err' * err;
mse = se / length(ytest);
stderr = std(err .* err) / sqrt(length(ytest));
fprintf('MSE (Ridge): %f\n', mse); 
fprintf('Standard Error (Ridge): %f\n', stderr);

%% Figure
dfs = dofRidge(X, Ks);
errorbar(dfs,mu,see)
hold on
plot(Kstar*ones(length(mu)+1,1),[0 mu]);