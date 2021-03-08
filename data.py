# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061136.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.
target_data = [list(filter(lambda item: item['station_id']=='C0A880',data))[0], list(filter(lambda item: item['station_id']=='C0F9A0',data))[0],list(filter(lambda item: item['station_id']=='C0G640',data))[0],list(filter(lambda item: item['station_id']=='C0R190',data))[0], list(filter(lambda item: item['station_id']=='C0X260',data))[0]]
mean_val = [list(filter(lambda item: item['station_id']=='C0A880',data))
		, list(filter(lambda item: item['station_id']=='C0F9A0',data))
		, list(filter(lambda item: item['station_id']=='C0G640',data))
		, list(filter(lambda item: item['station_id']=='C0R190',data))
		, list(filter(lambda item: item['station_id']=='C0X260',data))]

ans = []
for i in range(5):
    l = [float(x['PRES']) for x in mean_val[i]]
    a = 0
    b = 0
    k = len(l)
    for j in range(k):
        if l[j] != -99.0 and l[j] != -999.0:
            a = a + l[j]
            b = b
        else:
            a = a
            b = b + 1
    if (len(l)-b) != 0:
        ans.append([target_data[i]['station_id'], round(a/(len(l)-b),2)])
    else:
        ans.append([target_data[i]['station_id'], 'none'])
ans = sorted(ans)		  	
#=======================================

# Part. 4
#=======================================
# Print result
#========================================
print(ans)