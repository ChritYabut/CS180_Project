import csv
import numpy


def createMatrix(items, sales, dates):
	h = open("2017data.csv", "w")
	row = numpy.empty(items.size + 7)
	row.fill(0)
	Mat = []
	# print(sales)
	# count = 0
	for k in dates:
		for i in sales:
			if (k == i[3]):
				for j in items:
					if  i[2] == j:
						elem = numpy.where(items == j)
						row[elem[0][0]] = row[elem[0][0]]+1
						# print("went here")

		Mat.append(row)
		row = numpy.empty(items.size + 7)
		row.fill(0)
	with h:
		writer = csv.writer(h)
		writer.writerows(Mat)
		
		# count +=1
		# if (count > 200):
		# 	break
	h.close()


f = open("items.csv", "r")
g = open("2017.csv", "r")
itemsreader = csv.reader(f, delimiter = ',')
salesreader2015 = csv.reader(g, delimiter = ',')
items = set()
sales = []
days = []
recur = []
for row in itemsreader:
	items.add(row[0])

for day in salesreader2015:
	if (day[3] == 'TransDate'):
		continue
	sales.append(day)
	days.append(day[3])
	

dates = numpy.array(days)
rows = numpy.array(list(sorted(items)))
for i in dates:
	if (i in recur):
		continue
	else:
		recur.append(i)
dates = numpy.array(recur)
createMatrix(rows, sales, dates)

f.close()
g.close()
# for row in salesreader2015:
# 	print(row)