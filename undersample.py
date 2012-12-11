from collections import Counter
import numpy as np


counter = Counter(y)
num_neg = counter[counter.keys()[0]]
num_pos = counter[counter.keys()[1]]

n_samples = len(y)

#positives = [y[i]>0 for i in range(len(y))]
#negatives = [y[i]>0 for i in range(len(y))]

positives = []
negatives = []
for i in range(n_samples):
	if y[i] > 0:
		positives.append(i)
	else:
		negatives.append(i)

counter_samples = []
if num_neg > num_pos:
	for i in range(len(positives)):
		counter_samples.append(np.random.randint(len(negatives)))
else:
	for i in range(len(negatives)):
		counter_samples.append(np.random.randint(len(positives)))

balanced_X = np.concatenate((X[positives], X[counter_samples]))
balanced_y = np.concatenate((y[positives], y[counter_samples]))

#balanced_X = np.array(X[positives].tolist()+X[counter_samples].tolist())
#balanced_y = np.array(y[positives].tolist()+y[counter_samples].tolist())
index = np.arange(0,len(balanced_X))
np.random.shuffle(index)
balanced_X = balanced_X[index]
balanced_y = balanced_y[index]