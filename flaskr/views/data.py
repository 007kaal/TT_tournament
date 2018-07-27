from csv import DictWriter, DictReader

WS_FILE="flaskr/CSVData/ws.csv"
MS_FILE="flaskr/CSVData/ms.csv"
MD_FILE="flaskr/CSVData/md.csv"
WD_FILE="flaskr/CSVData/wd.csv"
XD_FILE="flaskr/CSVData/xd.csv"


WS = []
WD = []
MS = []
MD = []
XD = []


def read_data():
  with open(WS_FILE) as csvFile:
      global WS
      reader = DictReader(csvFile)
      for line in reader:
           WS.append(line)

  with open(MS_FILE) as csvFile:
      global MS
      reader = DictReader(csvFile)
      for line in reader:
           MS.append(line)

  with open(WD_FILE) as csvFile:
      global WD
      reader = DictReader(csvFile)
      for line in reader:
           WD.append(line)

  with open(MD_FILE) as csvFile:
      global MD
      reader = DictReader(csvFile)
      for line in reader:
           MD.append(line)

  with open(XD_FILE) as csvFile:
      global XD
      reader = DictReader(csvFile)
      for line in reader:
           XD.append(line)

def get_upcomming_matches(category):
  if category == "WS":
     return [ X for X in WS if X['result'] == "YTP"]
  elif category == "WD":
     return [ X for X in WD if X['result'] == "YTP"]
  elif category == "MS":
     return [ X for X in MS if X['result'] == "YTP"]
  elif category == "MD":
     return [ X for X in MD if X['result'] == "YTP"]
  elif category == "XD":
     return [ X for X in XD if X['result'] == "YTP"]
  else :
      return []

def get_results(category):
  if category == "WS":
     return [ X for X in WS if X['result'] != "YTP"]
  elif category == "WD":
     return [ X for X in WD if X['result'] != "YTP"]
  elif category == "MS":
     return [ X for X in MS if X['result'] != "YTP"]
  elif category == "MD":
     return [ X for X in MD if X['result'] != "YTP"]
  elif category == "XD":
     return [ X for X in XD if X['result'] != "YTP"]
  else :
      return []
  


def update_file(Fname, DictList):
  fieldnames = ['id', 'team1', 'team2', 'time', 'result']
  with open(Fname, 'w') as  csvFile:
      writer = DictWriter(csvFile, fieldnames = fieldnames)
      writer.writeheader()
      for line in DictList:
         writer.writerow(line)


read_data()
update_file("ws.csv", WS)
