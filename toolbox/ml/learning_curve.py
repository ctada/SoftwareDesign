""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

num_trials = 50
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner
data = load_digits()
for i,percent in enumerate(train_percentages):
	for trial in range(num_trials):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=percent*.01)
		model = LogisticRegression(C=10**-10) # Inverse of regularization strength, smaller values specify stronger regularization.
		model.fit(X_train, y_train)

		#print "Train accuracy %f" %model.score(X_train,y_train)
		test_accuracies[i] += model.score(X_test,y_test)
	test_accuracies[i]=float(test_accuracies[i])/num_trials #averaging test accuracy

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()
