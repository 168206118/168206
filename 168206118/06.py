# -*- coding: UTF-8 -*-
start = 'hit'
end = 'cog'

adict = ['hot','dot','dog','lot','log']

def find_path(start, end, paths):
	if start==end:
		
		return "start==end"
	
	else:
		visited=[]
		visited.append(start)
		for word in visited:
				for i in range(len(word)):
					for j in range(ord('a'),ord('z')+1):
							word=word[:i]+chr(j)+word[i+1:]
								    if word in paths and word not in visited:
										  visited.append(word)
										  print(word)
								    if word==end:
										  print("the end is  "+word)
								 		  return	
								                                      
find_path(start,end,adict) 
