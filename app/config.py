import pymongo

# myclient = pymongo.MongoClient("mongodb://192.168.192.38:27017/")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dbPerfENERGIE = myclient["perf_energ"]
# dbPerfRSE = myclient["Perf-RSE"]