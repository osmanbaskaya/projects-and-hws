clear; clc; close all
data = csvread('Input.txt');
X = data(:, 1:2);
y = data(:, 3);

%% Q1 - Plot the data
figure1 = figure;
idx1 = y == 1;
idx0 = y == 0;

plot(X(idx1, 1), X(idx1, 2), 'bo');
hold on;
plot(X(idx0, 1), X(idx0, 2), 'rx');


%% Q2 - Draw lines


hold on;
num_p = 25;
yy = linspace(2,6,num_p);
x = ones(num_p, 1) .* -2.555;
plot(x, yy, '-');

hold on;
yy = linspace(6, 8, num_p);
% Create line
annotation(figure1,'line',[0.208823529411765 0.45],...
    [0.60890990990991 0.759549549549549]);

% Create line
annotation(figure1,'line',[0.451470588235294 0.591176470588235],...
    [0.759549549549549 0.72972972972973]);

% Create line
annotation(figure1,'line',[0.589705882352941 0.566176470588235],...
    [0.724225225225225 0.558558558558559]);

% Create line
annotation(figure1,'line',[0.561764705882353 0.607352941176471],...
    [0.555306306306306 0.504504504504504]);

% Create line
annotation(figure1,'line',[0.619117647058824 0.486764705882353],...
    [0.494495495495495 0.274774774774775]);

% Create line
annotation(figure1,'line',[0.205882352941176 0.292647058823529],...
    [0.442693693693694 0.436936936936937]);

% Create line
annotation(figure1,'line',[0.3 0.401470588235294],...
    [0.431432432432432 0.351351351351351]);

% Create line
annotation(figure1,'line',[0.401470588235294 0.482352941176471],...
    [0.348099099099099 0.261261261261261]);

% Create line
annotation(figure1,'line',[0.208823529411765 0.208823529411765],...
    [0.44945045045045 0.436936936936937]);

% Create line
annotation(figure1,'line',[0.489705882352941 0.480882352941176],...
    [0.276027027027027 0.261261261261261]);

% Create line
annotation(figure1,'line',[0.604411764705882 0.617647058823529],...
    [0.505756756756757 0.490990990990991]);

% Create line
annotation(figure1,'line',[0.291176470588235 0.307352941176471],...
    [0.435936936936937 0.423423423423423]);



%% Q3 - If-Else

mx = 1.8;
my = 4;

best_r = 0;
best_accuracy = -1;
% Optimization for r (radius)
for r=1.5:0.02:4
    predictions = predict(X, mx, my, r);
    total = length(y);
    n_true = sum(~xor(predictions, y));
    accuracy = n_true / total;
    fprintf('Accuracy %.3f\t%.1f, %.1f, %.1f\n', accuracy, mx, my, r);
    if best_accuracy < accuracy
        best_accuracy = accuracy;
        best_r = r;
    end
end

% Reporting the best accuracy:
fprintf('\nBest Accuracy %.3f\t%.1f, %.1f, %.1f\n\n', ...
    best_accuracy, mx, my, best_r);

% Confusion Matrix 
predictions = predict(X, mx, my, r);
total = length(y);
true_pos = sum(~xor(predictions(idx1), y(idx1)));
num_pos = sum(y(idx1));
num_neg = sum(~y(idx0));
true_neg = sum(~xor(predictions(idx0), y(idx0)));
false_neg = num_pos - true_pos;
false_pos = num_neg - true_neg;

fprintf('True Positive: %d\t True Negative: %d\nFalse Positive: %d\t False Negative: %d\n', ...
        true_pos, true_neg, false_pos, false_neg);

