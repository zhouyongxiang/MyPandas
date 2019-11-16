

L = [
 ['Apple', 'Google', 'Microsoft'],
 ['Java', 'Python', 'Ruby', 'PHP'],
 ['Adam', 'Bart', 'Lisa',[1,2,3,[4,5]]]
]

def li(k):
	for i in k:
		if not isinstance(i,list):
			print(i)
		else:
			li(i)
			
            
li(L)