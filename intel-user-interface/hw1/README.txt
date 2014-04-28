HW1 - Osman Baskaya

HW1 consists of three parts. 

First and second parts are fairly straightforward and
hopefully code is clear.

Third part deserves some explanation.

My model is a circle, that is, I fit a circle for this problem.
Circle has three parameters, mx, my, and r (radius).

M(1.8, 4.0) is taken as circle's center point. For radius,
I made a line search in order to find the best r given M and
for this setting, the best r equals to 3.1.

So best parameter setting is mx=1.8, my=4.0, and r=3.1.
According to this model my accuracy is .851. My confusion matrix
is as follows:

True Positive (1, 1): 541	 True Negative (0,0): 575
False Positive(Actual class=0, Predictions=1): 25
False Negative(Actual class=1, Predictions=0): 259

This is fairly simple yet effective. I really don't go with
lots of if statement since this kind of fine tuning makes the model
overfit the training data. My model is more general and 
if we have a test set I can say that my model's accuracy will be
higher than an overfitted models.


# End of the document.
