string = "hello"

integer = 5

float_ = 5.5

bool_ = True

list_ = [1, 2, 3]

dict_ = {"name": "John", "age": 25}

tuple_ = (1, 2, 3)

None_ = None

var = string == integer == float_ == bool_ == list_ == dict_ == tuple_ == None_

num_str = 125

num_str = str(num_str)

print(num_str)

message = 'Hi, my name is Python!'

message = message.replace("y", "0")
message = message.replace("i", "1")

print(message)

split_test = 'This is a split test'
split_test = split_test.split(' ')
print(split_test)
string_join = " ".join(split_test)
print(string_join)
print(len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))
print(len(list_append))

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())

