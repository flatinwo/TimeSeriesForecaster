import timeseries as ts 
import numpy as np
import pandas as pd

class Returns:
	def __init__(self,data):
		assert isinstance(data,ts.TimeSeriesDF)

	@staticmethod
	def compute(data,colnames=["Open", "High", "Low", "Close"]):
		assert isinstance(data,ts.TimeSeriesDF)
		for name in colnames:
			data.df[name+str("Return")] = np.log(data.df[name]/data.df[name].shift())

		return data

class Volatilies:
	def __init__(self,data):
		self.vols = []
		self.transformed_by=""
		if isinstance(data,pd.core.groupby.DataFrameGroupBy):
			self.vols = Volatilies.compute(data)
		elif isinstance(data,ts.TimeSeriesDF):
			pass
		else:
			raise TypeError("Unexpected type error.")

	@staticmethod
	def compute(data,colnames=[s+str("Return") for s in ["Open", "High", "Low", "Close"]],method="std",pandas=True):
		if pandas: 
			return getattr(data[colnames],method)()
		else:
			pass

	def transform(self,function=None):
		if function is not None:  
			self.vols = function(self.vols)
			self.transformed_by += " + " + str(function)

	def annualize(self,factor=np.sqrt(252*288)):
		self.vols = self.vols*factor
		self.transformed_by += ("+ scaled by " + str(factor))



if __name__ == "__main__":
	tsdf = ts.TimeSeriesDF()
	tsdf_returns = Returns.compute(tsdf)
	vol = Volatilies(tsdf_returns.getDaily())
	vol.annualize()
	vol.transform(function=np.log)
	vol.vols.dropna(inplace=True)
