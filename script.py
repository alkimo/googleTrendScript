from pytrends.request import TrendReq
import string
import parseInput
import setSearchResult
import csvCore
import os
from datetime import datetime

args = parseInput.initParse()

keyword_list = [args.a, args.b, args.c, args.d, args.e]
keyword_list = [i for i in keyword_list if i] 

title = '+'.join(keyword_list) 

pytrend = TrendReq()
pytrend.build_payload(kw_list=keyword_list, cat = args.cat, timeframe = args.timeframe, geo = args.geo, gprop = args.gprop)

searchResultList = setSearchResult.getAllSearches(pytrend)

csvPath = os.getcwd() + '/CSVSearchResults/'
thisSearchDir = csvPath + title + '-' + datetime.now().strftime("%d") + '-' + datetime.now().strftime("%m") + '-' + datetime.now().strftime("%Y") + '-' + datetime.now().strftime("%X")
os.mkdir(thisSearchDir)

iot = searchResultList[0]
ibr = searchResultList[1]
rt = searchResultList[2]
rq = searchResultList[3]

csvCore.generateSimpleCSV(iot, 'iot', keyword_list, thisSearchDir)
csvCore.generateSimpleCSV(ibr, 'ibr', keyword_list, thisSearchDir)
csvCore.generateComplexCSV(rt, 'rt', thisSearchDir)
csvCore.generateComplexCSV(rt, 'rq', thisSearchDir)