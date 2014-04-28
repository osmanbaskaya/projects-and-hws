function [prior0 prior1 cond0 cond1] = ...
                    NaiveBayesParameterEst(X, y)


negative_class = sum(y == 0);
positive_class = sum(y == 1);

%% Prior Probability Estimations

prior0 = negative_class / (negative_class + positive_class);
prior1 = positive_class / (negative_class + positive_class);

%% Class Conditional Probability Estimation

neg_idx = y == 0;
pos_idx = y == 1;

neg_count = sum(X(neg_idx, :));
pos_count = sum(X(pos_idx, :));
total_count = neg_count + pos_count;

cond0 = neg_count ./ total_count;
cond1 = pos_count ./ total_count;



end

