
from scrapy import Selector

f = open('data.html','r')
body = f.read()
f.close()

a = Selector(text=body).xpath('//a/text()').extract()
b = Selector(text=body).xpath('//a/@href').extract()

for j in range(len(a)):
	a[j] = a[j].encode('utf-8')
	b[j] = b[j].encode('utf-8')

g = open('companies list.txt','w')

for i in range(len(b)):
	g.write(str(i+1) + '. ' + a[i] + ' - ' + b[i] + '\n')
	#print(a[i] + ' - ' + b[i])

g.close()

