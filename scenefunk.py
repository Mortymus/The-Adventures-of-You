
a='Du lukte vondt å e dårlige t beins.'
b='Du elske å springa maraton.'
ab='Du drømme om å få robotbein.'
aa='Du ska spleisa på ein rollestol med ein nabo.'
aaa='''Han hente deg i en stjålen bil.

Game over'''
aab='''Du leve tusen liv, 
det eina verre enn d andra...

Game over'''
ba='''Den styste skoffelsen for deg med 
koronaviruset e at du ikkje fekk delta 
i OL i Tokyo.'''
bb='''Du va på xxl, men de hadde ingen 
vekter så va tonge nåk.'''

c='''
Please press a or b,
(x to exit): '''
d='''
You have to enter a or b,
(x to exit): '''
e=('''
Thank you for playing :)''')
f=('''
Do you want to try again?

Press y for new game,
or x to exit: ''')
g='''
You have to press
y for new game,
or x to exit: '''

valg=''
valg2=''
valid=['a','b','x']
valg3=''
valid3=['y','x']

lista=['a','aa','aaa','aab','ab','b','ba','bb']
listasvar=[a,aa,aaa,aab,ab,b,ba,bb]
gameover=['aaa','aab']

while valg !='x':
	valg=input(c).lower()
	while valg not in valid:
		valg=input(d).lower()
	if valg in valid:
		valg2+=valg
		print(valg2)
		if valg2 in lista:
			print(listasvar[lista.index(valg2)])
			if valg2 in gameover:
				valg3=input(f).lower()
				while valg3 not in valid3:
					valg3=input(g).lower()	
				if valg3=='y':
					valg2=''
				if valg3=='x':
					break
print(e)
