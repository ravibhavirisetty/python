
# FLAMES calculator :)
# Raviteja Bhavirisetty

def FLAMES(name1,name2):
	name1.strip()
	name1 = name1.replace(' ','')
	name2.strip()
	name2 = name2.replace(' ','')
	flames = ['FRIENDS','LOVERS','AFFECTION','MARRIAGE','ENEMIES','SIBLINGS']

	s = set(name1)
	t = set(name2)
	common = s & t
	
	g = lambda i,j: i.replace(j,'')
	for i in common:
		name1 = g(name1,i)
		name2 = g(name2,i)
	count = len(name1) + len(name2)
	m = len(flames)

	while m > 2:
		m = len(flames)
		n = (count%m) - 1
		flames.pop(n)
	
	flames = ''.join(flames)
	return flames


print 'Welcome to FLAMES calculator!'
person1 = raw_input('Enter the first name: ')
person2 = raw_input('Enter the second name: ')
result = FLAMES(person1.lower(),person2.lower())
print "\nIt is '" + result + "' for " + person1 + ' and ' + person2 + '.'
print 'P.S.: If the result is in your favor, belive it. Chuck it otherwise! ;)\n'



