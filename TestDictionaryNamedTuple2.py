from collections import namedtuple
import pprint
import csv

filein = open("ReportingStructure.csv")
datadict={}
resultDict={}
resultList=[]
dict_data={}
resultDictNew={}
resultListNew=[]

headerline = [f.strip() for f in filein.readline().split(',')]
#print("headerline is:")
#print (headerline)

EmployeeRec=namedtuple('EmployeeRec',headerline)
for data in filein:
    data=[f.strip() for f in data.split(',')]
    #print(data)
    d=EmployeeRec(*data)
    datadict[d.TRDR_ID]=d

#print('details')
#print (datadict['rajkgupt'].EMP_FULL_NM)

csv_columns = ['TRDR_ID','SUB_DEPT_NM','EMP_FULL_NM','EMP_TYP_DESC','LEVEL_DESC','LEVEL_5',
               'MGR1_FUll_NM','MGR1_LEVEL_DESC','MGR1_LEVEL_5','MGR2_FULL_NM','MGR2_LEVEL_DESC','MGR2_LEVEL5']

csv_file = "Results.csv"

for key,value in  datadict.items():
    if key == 'bobby' or key == 'bobnew' or key=='sandip':
        break
    else:
        #print('%s\t %s\t %s\t %s\t %s' %(value.EMP_FULL_NM,value.EMP_TYP_DESC,value.LEVEL_DESC,value.LEVEL_5,value.MGR_TRDR_ID))
        #print(datadict[value.MGR_TRDR_ID].EMP_FULL_NM)
        resultDict[key] = value
        resultDict[value.MGR_TRDR_ID] = datadict[value.MGR_TRDR_ID]
        resultList += [resultDict]

        '''mgrRecord = EmployeeRec(datadict[value.TRDR_ID],datadict[value.SUB_DEPT_NM],datadict[value.EMP_FULL_NM],
                                datadict[value.EMP_TYP_DESC],datadict[value.LEVEL_DESC],datadict[value.LEVEL_5],
                                datadict[value.MGR_TRDR_ID])                                
        print(mgrRecord.MGR_TRDR_ID)'''

        empShortId=key
        empRecDetailsForResult=[value.EMP_FULL_NM,value.EMP_TYP_DESC,value.LEVEL_DESC,value.LEVEL_5,value.MGR_TRDR_ID]

        empRecDetailsForResult.append(datadict[value.MGR_TRDR_ID].EMP_FULL_NM)
        empRecDetailsForResult.append(datadict[value.MGR_TRDR_ID].LEVEL_DESC)
        empRecDetailsForResult.append(datadict[value.MGR_TRDR_ID].LEVEL_5)

        empRecDetailsForResult.append(datadict[datadict[value.MGR_TRDR_ID].MGR_TRDR_ID].EMP_FULL_NM)
        empRecDetailsForResult.append(datadict[datadict[value.MGR_TRDR_ID].MGR_TRDR_ID].LEVEL_DESC)
        empRecDetailsForResult.append(datadict[datadict[value.MGR_TRDR_ID].MGR_TRDR_ID].LEVEL_5)

        resultListNew = [key, empRecDetailsForResult]
        #print("resultListNew", resultListNew)


        resultDictNew[key] = empRecDetailsForResult



        dict_data = [
        {'TRDR_ID': key,'EMP_FULL_NM': value.EMP_FULL_NM, 'EMP_TYP_DESC': value.EMP_TYP_DESC, 'LEVEL_DESC': 'Vice President', 'LEVEL_5': 'India',
         'MGR1_FUll_NM': 'Ramesh Ramaswamy','MGR1_LEVEL_DESC':'Vice President','MGR1_LEVEL_5':'New York',
        'MGR2_FULL_NM':'Anil Sharma','MGR2_LEVEL_DESC':'Executive Director','MGR2_LEVEL5':'New York'},

        ]
pprint.pprint(resultDictNew)

try:
    with open(csv_file, 'w+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")














