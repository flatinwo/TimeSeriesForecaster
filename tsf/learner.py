import numpy as np
import scipy as sp
from sklearn.metric import mean_squared_error,log_loss

class StatLearner:
	def __init__(self):
		pass

	@staticmethod
	def previousRegresser(x):
		pass

	@staticmethod
	def linearRegresser(x):
		pass

	@staticmethod
	def aRCH(x,index=(1,1)):
		pass

	@staticmethod
	def gARCH(x,index=(1,1)):
		pass

	@staticmethod
	def neuralNet(x,network):
		pass

	@staticmethod
	def logisticRegresser(x):
		pass

	@classmethod
	def train(self, x):
		pass


class PerformanceMeasure:
	def __init__(self):
		pass


	@staticmethod
	def MeanSquareError(predicted, observed):
		return mean_squared_error(observed,predicted)


	@staticmethod
	def QausiLikelihood(predicted, observed):
		return log_loss(observed,predicted)

	def get(predicted,observed,name=["MSE","QSL"]):
		pass

