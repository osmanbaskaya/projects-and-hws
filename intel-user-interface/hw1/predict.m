function predictions = predict(X, mx, my, r)

predictions = (X(:,1) - mx).^2 + (X(:,2) - my).^2 > r^2;

end