students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
string = ''
for count in students:
	for key,data in count.iteritems():
		string +=data
		string +=' '
	print string
	string = ''

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
string = ''
i = 1
length = 0
for key,data in users.iteritems():
	print key
	for value in data:
		string = value['first_name'] + ' '+ value['last_name']
		length = len(string) - 1

		print i,'-',string,'-',length
		i +=1
	i = 1



