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
	def linearRegresser(x,colname="CloseReturn",training_size=4,n_params=3,asPandas=True,keep=False,function=np.log,inverse=np.exp):
		"""
		:param x includes data preferably as pd.core.frame.DataFrme
		:param training_size is the number of observations for regression
		:param number of regressors or features
		:returns depending on flag pandas data frame as result
		"""
		assert isinstance(x,pd.core.frame.DataFrame)
		assert colname in x.columns
		
		# construct observation and response matrix
		obs= function(x[colname]).as_matrix()
		sz=len(obs)-n_params+1
		obMatrix = np.array([obs[i:sz+i] for i in range(n_params)]).transpose()[:-n_params+1]
		respVector = obs[n_params:]

		assert len(obMatrix) == len(respVector)-1

		# create linear regression object
		from sklearn import linear_model
		regr = linear_model.LinearRegression()

		counter = 0
		sz = len(obMatrix)
		pred = np.zeros(sz-training_size-1)
		obs = np.zeros(sz-training_size-1)
		name="linearRegresser_"+str(n_params)
		regrparams=[]*(sz-training_size-1)

		# there is probably a clever to change state of regr without repassing data
		while counter + training_size < sz - 1 :
			regr.fit(obMatrix[counter:counter+training_size],
				respVector[counter:counter+training_size])

			pred[counter] = inverse(regr.predict(obMatrix[counter+training_size].reshape(1,-1))[0])
			obs[counter] = 	inverse(respVector[counter+training_size])
			counter += 1
			regrparams.append([regr.intercept_]+[regr.coef_])
		
		if asPandas:
			regresslog = pd.DataFrame(Analysis(pred,obs,keep=False,params={'all_coeffs':regrparams}).analyze,index=[name])
		else:
			regresslog = Analysis(pred,obs)
		return regresslog


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


if __name__ == "__main__":
	import timeseries as tf
	from volproxy import *

	tsdf = ts.TimeSeriesDF()
	tsdf_returns = Returns.compute(tsdf)
	vol = Volatilies(tsdf_returns.getDaily())
	vol.annualize()
	#vol.transform(function=np.log)
	vol.vols.dropna(inplace=True)
	Ans = StatLearner.linearRegresser(vol.vols)
