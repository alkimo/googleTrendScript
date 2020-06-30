def setIOT(searchResult):
    return searchResult.interest_over_time()

def setIBR(searchResult):
    return searchResult.interest_by_region()

def setRT(searchResult):
    return searchResult.related_topics()

def setRQ(searchResult):
    return searchResult.related_queries()

def getAllSearches(pytrend):
    interest_over_time = setIOT(pytrend)
    interest_by_region = setIBR(pytrend)
    related_queries = setRQ(pytrend)
    related_topics = setRT(pytrend)
    searchList = [interest_over_time, interest_by_region, related_queries, related_topics]
    return searchList