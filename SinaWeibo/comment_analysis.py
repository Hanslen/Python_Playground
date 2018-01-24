import pymysql
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np
conn = pymysql.connect(host='127.0.0.1',user='root',password='',charset='utf8')
with conn:
	cur = conn.cursor()
	cur.execute("SELECT * FROM sinaweibo.macomment")
	rows = cur.fetchall()
commentlist = []
for row in rows:
	row = list(row)
	del row[0]
	if row not in commentlist:
		commentlist.append(row[2])
conn.close()
print("Finish fetching the comment data...")
# print(commentlist)

# snowanalysis
print("Start SnowNLP data")
sentimentslist = []
for com in commentlist:
	s = SnowNLP(com)
	sentimentslist.append(s.sentiments)
	
# print(sentimentslist)
plt.hist(sentimentslist,bins=np.arange(0,1,0.02))
plt.show()