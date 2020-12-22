#TODO: import StopWatch

# example: generateMiddle(20,10,1)
def genMiddle(diskCount, rodCount, target):
	iter = diskCount - 1 	# свободных штырей == кол-во итераций
	rodRange = [] 			# лист возможных штырей кроме 0 и target
	for r in range(1,rodCount):
		if r != target:
			rodRange.append(str(r))
	
	nodeList = genOnRod(diskCount - 1, str(target), rodRange) # ! ВСЕМ ПИЗДЕЦ!!!
	# print("nodeList: {0}".format(nodeList))
	return nodeList
	
# position - disk position
# nodeTail - builded node str
# rodRange - list of rod str indices, except src and dst
def genOnRod(position, nodeTail, rodRange):
	newNodes = []
	# print("pos: {0} tail: {1} range: {2}".format(position, nodeTail, rodRange))	

	if position == 0:
		for r in rodRange:
			newNodes.append(r + nodeTail)
		return newNodes

	else:
		for r in rodRange:
			res = genOnRod(position - 1, r + nodeTail, rodRange)
			# print("res: {0}".format(res))
			if res != []:
				newNodes.extend(res)
	
		return newNodes
			
	
if __name__ == "__main__":
	nList = genMiddle(8,8,1)

	print(len(nList))
	if len(nList) != len(set(nList)):
		print('DUPLICATES!!!')
	else:
		print('NO DUPLICATES'.lower())

	
	
	
	