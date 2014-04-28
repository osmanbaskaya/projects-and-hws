function hw2
clc, clear, close all;

load bayesFactorGeneData.mat;

%% Question 1.a Ploting the data

plotData(Xcontrol);
plotData(Xtreat);

%% Question 1.b Calculating Bayes factos and the p-values

m = length(truth);
bf = zeros(m, 1);
pvals = zeros(m, 2);

for g=1:m
    bf(g) = bayesianTtest(Xtreat(g, :), Xcontrol(g, :));
    [pvals(g, 1), pvals(g, 2)] = ttest(Xtreat(g, :), Xcontrol(g, :));
    %pvals(g, :) = ttest(Xtreat(g, :), Xcontrol(g, :));
end

figure,
plot(1:100, log(1./bf), '-b');
figure,
plot(1:100, 1./pvals(:,2), '-g');

%% Question 2: 

[bf_false, bf_hit, ~] = ROCcurve(log(1./bf), truth, 0);
[pval_false, pval_hit, ~] = ROCcurve(log(1./pvals(:,2)), truth, 0);
plot(bf_false, bf_hit, '--b');
hold on; grid on;
xlabel('false rate')
ylabel('hit rate')
legend
plot(pval_false, pval_hit, '--r');

%% Question 3:

close all
Xtreat_sorted = sortrows([truth', Xtreat]);
Xtreat_sorted = Xtreat_sorted(:, 2:3);
Xcontrol_sorted = sortrows([truth', Xcontrol]);
Xcontrol_sorted = Xcontrol_sorted(:, 2:3);
plotData(Xcontrol_sorted);
plotData(Xtreat_sorted);


m = length(truth);
bf_sorted = zeros(m, 1);
pvals_sorted = zeros(m, 2);

for g=1:m
    bf_sorted(g) = bayesianTtest(Xtreat_sorted(g, :), Xcontrol_sorted(g, :));
    [pvals_sorted(g, 1), pvals_sorted(g, 2)] = ttest(Xtreat_sorted(g, :), Xcontrol_sorted(g, :));
    %pvals(g, :) = ttest(Xtreat(g, :), Xcontrol(g, :));
end

figure,
plot(1:100, log(1./bf_sorted), '-b');
figure,
plot(1:100, 1./pvals_sorted(:,2), '-g');

end


% Helper method for plotting.
function plotData(data)
figure;
plot(1:100, data(:, 1), '-b');
hold on;
plot(1:100, data(:, 2), '-g');
end

