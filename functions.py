import numpy as np
import math

# prints formatted price
def formatPrice(n):
	return ("-KRW " if n < 0 else "KRW ") + "{}".format(abs(n))

# returns the vector containing stock data from a fixed file
def getStockDataVec(key):
	vec = []
	lines =  open("data/" + key + ".csv", "r").read().splitlines()
	for line in lines[1:]:
		close = line.split(",")[-1]
		if close and close != 'null':
			vec.append(float(close))
	return vec
	# modified
	# lines = open("data/" + key + ".csv", "r").read().splitlines()
	#
	# for line in lines[1:]:
	# 	close = line.split(",")[4]
	# 	if close != 'null':
	# 		vec.append(float(line.split(",")[4]))

	return vec

# returns the sigmoid
def sigmoid(x):
	if -x > np.log(np.finfo(type(x)).max):
		return 0.0
	else:
		return 1 / (1 + np.exp(-x))

# returns an an n-day state representation ending at time t
def getState(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i]))

	return np.array([res])
