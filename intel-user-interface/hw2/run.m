function accuracies = run(data, k, train_params, kernel)

CV0 = cvpartition(data(:, end), 'KFold', k);
cost = 2 .^ (-1:10);
gamma = 2.^ (-10:1:-1);
accuracies = zeros(k,1);


predictions = [];
actual_labels = [];
ndata = [];

for i=1:k
    test = data(CV0.test(i), :);
    CV1 = cvpartition(data(CV0.training(i),end), 'KFold', k);
    best_score = -1;
    val_accuracies = zeros(length(gamma), length(cost));
    for j=1:k
        validation = data(CV1.test(j), :);
        val_training = data(CV1.training(j), :);
        for ci=1:length(cost)
            for gi=1:length(gamma)
                c = cost(ci);
                g = gamma(gi);
                params = sprintf(train_params, c, g);
                fprintf('%s\n', params);
                model = svmtrain(val_training(:,end), val_training(:, 1:end-1), params);
                [p_label, accuracy, ~] = svmpredict(validation(:,end), validation(:, 1:end-1), model, '');
                val_accuracies(gi, ci) = val_accuracies(gi, ci) + accuracy(1);
            end
        end
    end
        val_accuracies = val_accuracies / k;
        training = data(CV0.training(i), :);
        max_val_accuracy = max(max(val_accuracies));
        [gi_max, ci_max] = find(val_accuracies == max_val_accuracy);
        g_max = gamma(gi_max(1));
        c_max = cost(ci_max(1));
        imagesc(val_accuracies);
        fn = sprintf('Validation-%s-Chunk%d.jpg', kernel, i);
        title(fn);
        print('-djpeg', fn);
        params = sprintf(train_params, c_max, g_max);
        %title(sprintf('Parameters: %s' params);
        model = svmtrain(training(:,end), training(:, 1:end-1), params);
        [p_label, accuracy, ~] = svmpredict(test(:,end), test(:, 1:end-1), model, '');
        predictions = [predictions; p_label];
        actual_labels = [actual_labels; test(:, end)];
        ndata = [ndata; test(:, 1:end-1)];
        accuracies(i) = accuracy(1);
        model_filename = sprintf('%s-chunk-%d.model', kernel, i);
        save(model_filename, model);
end

close all;
figure; hold on;
plot(ndata(predictions == actual_labels), 'bo') 
plot(ndata(predictions ~= actual_labels), 'rx') 
tit = sprintf('Prediction accuracy: %.2f', mean(accuracies));
title(tit);

legend('Correct Predictions', 'Wrong Predictions')


end