import timeseries as ts 
import numpy as np

class Returns:
	def __init__(self,data):
		assert isinstance(data,ts.TimeSeriesDF)

	@staticmethod
	def compute(data,colnames=["Open", "High", "Low", "Close"]):
		assert isinstance(data,ts.TimeSeriesDF)
		for name in colnames:
			data.df[name+str("Return")] =
			np.log(data.df[name]/data.df[name].shift())

		return data

class Volatilies:
	def __init__(self,data):
		self.vols = Volatilies.compute(data)

	@staticmethod:
	def compute(data,colnames=[s+str("Return") for s in ["Open", "High", "Low", "Close"]],method="std",pandas=True):
		if pandas: 
			return getattr(data[colnames],method)()
		else:
			pass


