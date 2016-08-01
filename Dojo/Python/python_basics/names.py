#names part 1

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for val in students:
#     print val["first_name"] , val["last_name"]


#names part 2
#key within a key
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


# for key,data in users.items():
#     count = 0
#     sum = 0
#     print key
#     for value in data:
#         count += 1
#         sum = len(value["first_name"]) + len(value["last_name"])
#         print count, value["first_name"] , value["last_name"], sum

for key, data in users.items():
    for num, value in enumerate(data):
        print num+1, value["first_name"], value["last_name"], len(value["first_name"] + value["last_name"])