import pandas as pd

class TimeSeriesDF:
	def __init__(self,filename="../data/AUDUSD.csv"):
		self.df = pd.read_csv(filename)
		dt = self.df.Date.astype(str).str.cat(self.df.Time.astype(str), sep=' ')
		pd.to_datetime(dt)
		self.df.set_index(pd.Series(dt),inplace=True)

	def spread(self):
		pass


if __name__ == "__main__":
	tsdf = TimeSeriesDF()