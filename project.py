import numpy as np

class getdata(object): #to get any one-year timeseries data from csv
    def __init__(self, csvdata, timerange):
        self._csvdata = csvdata
        self._timerange = timerange
    
    def givedata(self):
        return (np.genfromtxt(self._csvdata,delimiter=','))
    
    def resolution(self): #in hour
        return (8760/self._timerange)

class getvar(getdata):
    def __init__(self, csvdata, timerange, inputvar):
        super(getvar,self).__init__(csvdata, timerange)
        self._inputvar = inputvar
    
    def theprof(self): #the time-series profile
        return(self.givedata())
    
    def theres(self): #the data resolution
        return(self.resolution())
    
    def intracorr(self): #the intra-var corr
        return(np.corrcoef(self.givedata(), rowvar=False))
        
    def inputtype(self):
        return (self._inputvar)

def intercorr(var1,var2):
    corr = []
    for i in range(len(var1[0])-1):
        x = np.corrcoef(var1[:,i+1],var2[:,i+1])[1][0]
        print(x)
        corr = corr+[x]
    return (corr)

loaddata = getvar ('household_load.csv',35040,'load')
pvdata = getvar ('solar_production.csv',35040,'pv')
interc = intercorr(loaddata.theprof(),pvdata.theprof())
