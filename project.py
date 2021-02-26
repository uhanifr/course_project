'this program calculates the intra-variable and inter-variable of power system input.'
'the input is one-year data of household load, PV generation, and EV charging'
'the size of these inputs should be the same'

import numpy as np

class getdata(object): #to get any one-year timeseries data from csv
    def __init__(self, csvdata, timerange):
        self._csvdata = csvdata
        self._timerange = timerange
    
    def givedata(self):
        return (np.genfromtxt(self._csvdata,delimiter=','))
    
    def resolution(self): #in hour
        return (8760/self._timerange)

class getvar(getdata): #to get the variables.
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

def intercorr(var1,var2): #to get the correlation from two different variables
    corr = []
    for i in range(len(var1[0])-1):
        x = np.corrcoef(var1[:,i+1],var2[:,i+1])[1][0]
        print(x)
        corr = corr+[x]
    return (corr)

#example

#get the load data from 15 minutes resolution-one year data
loaddata = getvar ('household_load.csv',35040,'load')

#get the pv data from 15 minutes resolution-one year data
pvdata = getvar ('solar_production.csv',35040,'pv')

#some information that can be taken is time-series profile as np.array, resolution, and the intra-variable correlation
loadintracorr = loaddata.intracorr() #intra-correlation of load
pvintracorr = pvdata.intracorr() #intra-correlation of PV

#inter-variable correlation between load and pv
interc = intercorr(loaddata.theprof(),pvdata.theprof())
