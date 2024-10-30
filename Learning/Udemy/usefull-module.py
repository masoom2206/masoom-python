from collections import Counter, defaultdict, OrderedDict

# li = [1, 2, 3, 2, 4, 4, 6, 7, 8, 7]
# print(Counter(li))# Its return the count of every number in dictionary

# sen = "Blah Blah B;ah I am thinking about python."
# print(Counter(sen))

# dic = {'a': 1, 'b': 2}
# # dic = defaultdict(int, dic)# set the defaukt vakue as 0
# # dic = defaultdict(lambda: 3, dic)# set the defaukt vakue as 3
# dic = defaultdict(lambda: "Doesn't exist", dic)# set the defaukt vakue as 3
# print(dic['c'])


# dic1 = OrderedDict()
# dic1['a'] = 1
# dic1['b'] = 2
# dic1['c'] = 3

# dic2 = OrderedDict()
# dic2['a'] = 1
# dic2['b'] = 2
# dic2['c'] = 3

# print(dic1 == dic2)# True


# dic1 = OrderedDict()
# dic1['b'] = 2
# dic1['a'] = 1
# dic1['c'] = 3

# dic2 = OrderedDict()
# dic2['a'] = 1
# dic2['b'] = 2
# dic2['c'] = 3

# print(dic1 == dic2)# Fasle

dic1 = {}
dic1['b'] = 2
dic1['a'] = 1
dic1['c'] = 3

dic2 = {}
dic2['a'] = 1
dic2['b'] = 2
dic2['c'] = 3

print(dic1 == dic2)# True