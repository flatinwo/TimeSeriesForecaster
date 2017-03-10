import numpy as np
import scipy as sp
from sklearn.metrics import mean_squared_error,log_loss
import pandas as pd

class StatLearner:
	def __init__(self):
		pass

	@staticmethod
	def previousRegresser(x,shift=1,colname="CloseReturn",name="",asPandas=False):
		assert isinstance(x,pd.core.frame.DataFrame)
		assert colname in x.columns
		pred = x.shift(shift)[colname].as_matrix()[shift:]
		obs = x[colname].as_matrix()[shift:]
		name = "previousRegresser"+str(name)
		return Analysis(pred,obs) if not asPandas else pd.DataFrame(Analysis(pred,obs,keep=False,params={'shift':shift}).analyze,index=[name])

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


class Analysis:
	def __init__(self,predicted,observed,params=None,keep=True,name=None):
		self.analyze = {}
		if keep:
			self.analyze['x_data'] = [[observed]]
			self.analyze['x_pred'] = [[predicted]]
		self.analyze['MSE'] = [PerformanceMeasure.MeanSquareError(observed,predicted)]
		self.analyze['MQL'] = [PerformanceMeasure.QuasiLikelihood(observed,predicted)]
		if params is not None: self.analyze["params"] = [params]
		if name is not None: self.analyze["instrument"] = [name]


class PerformanceMeasure:
	def __init__(self):
		pass


	@staticmethod
	def MeanSquareError(predicted, observed):
		return mean_squared_error(observed,predicted)


	@staticmethod
	def QuasiLikelihood(predicted, observed,normalize=False):
		return np.mean((predicted/observed - np.log(predicted/observed) - 1.))
	
	def get(predicted,observed,name=["MSE","QSL"]):
		pass

