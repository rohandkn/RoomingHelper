
import random

names = ['Daniel', 'Rohan', 'Raman', 'Jonathan', 'Vineet', 'Roy', 'Raj', 'Ravi']
defnames = ['Daniel', 'Rohan', 'Raman', 'Jonathan', 'Vineet', 'Roy', 'Raj', 'Ravi']

preferences = {}
room1 = []
room2 = []
minimum = 999
finalroom1 = []
finalroom2 = []

def start():
	global preferences
	#this
	preferences = {'Raman': ['Vineet', 'Roy'], 'Vineet': ['Roy', 'Daniel'], 'Raj': ['Daniel', 'Rohan'], 'Roy': ['Jonathan', 'Raman'], 'Daniel': ['Jonathan', 'Ravi'], 'Ravi': ['Jonathan', 'Roy'],'Rohan': ['Ravi', 'Vineet'], 'Jonathan': ['Raj', 'Ravi']}
	#or this
	# for name in names:
	# 	preferences[name] = []
	# 	preferences[name].append(raw_input(name+', who would you not like to room with?'))
	# 	preferences[name].append(raw_input(name+', who would you not like to room with?'))


	for i in xrange(0, 99999):
		rooms = randomRooms()
		checkScore(rooms[0], rooms[1])
	print "OPTIMAL ROOMING:"
	print "Room 1: "+str(finalroom1)
	print "Room 2: "+str(finalroom2)





def preference():
	for i in xrange(0, (len(names)-1)):
		preferences[names[i]] = []
		preferences[names[i]].append(raw_input('Enter a name'))
		preferences[names[i]].append(raw_input('Enter a name'))
		print preferences




def randomRooms():
	rooms1 = []
	rooms2 = []
	tempnames = ['Daniel', 'Rohan', 'Raman', 'Jonathan', 'Vineet', 'Roy', 'Raj', 'Ravi']

	while len(rooms1)<4:
		randomchoice = random.choice(tempnames)
		rooms1.append(randomchoice)
		tempnames.remove(randomchoice)
		randomchoice = random.choice(tempnames)
		rooms2.append(randomchoice)
		tempnames.remove(randomchoice)
	room = []
	room.append(rooms1)
	room.append(rooms2)
	return room

minimum = 9999
def checkScore(roo1, roo2):
	global preferences
	global minimum
	global finalroom1
	global finalroom2
	

	roomscore = 0
	for nameper in defnames:
		
		if(nameper in roo1 and preferences[nameper][0] in roo1):
			roomscore += 1
		if(nameper in roo1 and preferences[nameper][1] in roo1):
			roomscore += 1
		if(nameper in roo2 and preferences[nameper][0] in roo2):
			roomscore += 1
		if(nameper in roo2 and preferences[nameper][1] in roo2):
			roomscore += 1
	if(roomscore < minimum):
		finalroom1 = roo1
		finalroom2 = roo2
		print roo1
		print roo2
		print roomscore
		minimum = roomscore
	if(roomscore == minimum):
		if(roo1.sort()!=finalroom1.sort()):
			print roo1
			print roo2
	return roomscore

start()

	