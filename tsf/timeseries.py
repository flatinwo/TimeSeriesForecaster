import pandas as pd

class TimeSeriesDF:
	def __init__(self,filename="../data/AUDUSD.csv",infer_datetime_format=True,offsetHr=8,offsetMin=-5):
		self.df = pd.read_csv(filename)
		dt = self.df.Date.astype(str).str.cat(self.df.Time.astype(str), sep=' ')
		pd.to_datetime(dt,infer_datetime_format=infer_datetime_format)
		self.df.set_index(pd.DatetimeIndex(dt),inplace=True)
		self.df.index +=  pd.offsets.Hour(offsetHr) + pd.offsets.Minute(offsetMin)

	def getDaily(self):
		return self.df.groupby(pd.TimeGrouper(freq='D'))

	def getWeekly(self):
		return self.df.groupby(pd.TimeGrouper(freq='W'))

	def getMonthly(self):
		return self.df.groupby(pd.TimeGrouper(freq='M'))

	def getYearly(self):
		return self.df.groupby(pd.TimeGrouper(freq='12M'))

	def getPeriod(self):
		pass

	def resampleTrainAndTest(self):
		pass

	def spread(self):
		pass

	def getCustomTimeGroup(self):
		from pandas.tseries.offsets import CustomBusinessMonthBegin, CustomBusinessHour
		bh = CustomBusinessHour(start='16:00',weekmask='Sun Mon Tue Wed Thu Fri')
		#http://stackoverflow.com/questions/13019719/get-business-days-between-start-and-end-date-using-pandas
		#http://pandas.pydata.org/pandas-docs/stable/timeseries.html
		pass



if __name__ == "__main__":
	tsdf = TimeSeriesDF()