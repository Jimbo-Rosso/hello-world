#python ~/Documents/'more applications'/google/code_data_structures/crackingthecode/UniqueCharactersInaString.py

def uniquechars(mstring):
	mhashtable={}
	for char in mstring:
		#mhashtable[char]+=1
		if char in mhashtable.keys():
			mhashtable[char]+=1
			print('duplicate',char)
			return 'No'
		else:
			mhashtable[char]=1
	#if mhashtable.values>1: return 'No'
	return 'Si'
		

	


if __name__=="__main__":
	
	mstring='my stringl_=a'
	sol=uniquechars(mstring)

	print('mstring',mstring)
	print('sol',sol)
