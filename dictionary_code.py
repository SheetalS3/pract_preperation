'''---------------Convert two lists into a dictionary-------------'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def merge_toDict():
    dict1= {}
    for i in range(len(keys)):
        # dict1[keys[i]] = values[i]
        # dict1.update({keys[i]: values[i]})
        dict1= dict(zip(keys, values))
    print(dict1)
# merge_toDict()   

'''---------------Merge two Python dictionaries into one-----------'''

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}      

def merge2dict():
    # dict1.update(dict2) # print(dict1)
    dict3= {**dict1, **dict2}
    print(dict3)
# merge2dict()    

'''---------------Print the value of key ‘history’ from the below dict----------------'''
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# print(sampleDict["class"]["student"]["name"])
# print(sampleDict["class"]["student"]["marks"]["physics"])
# print(sampleDict["class"]["student"]["marks"]["history"])


'''---------------------Initialize dictionary with default values--------------------------'''

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

#op - {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

new_dict= {}
def initialize_values():
    for i in range(0, len(employees)):
        new_dict[employees[i]]= defaults
    print(new_dict)

# initialize_values()        


'''-----------------Sorting of dictionary------------------'''

my_Dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
d= {}
def sort_dict(myDict):
    keys_fun= myDict.keys()
    keys_lst= list(keys_fun)
    keys_lst.sort()
    for i in keys_lst:
        d.setdefault(i, myDict[i])
    print(d)
    # sorted_dict= {i:myDict[i] for i in keys_lst} 
    # print(sorted_dict)    
# sort_dict(my_Dict)

'''----------create a new dictionary by extracting the mentioned keys from the below dictionary.----------'''

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# Keys to extract
keys = ["name", "salary"]   # O/p - {'name': 'Kelly', 'salary': 8000}

#Logic - lst var for loop till length. new dict madhe dict2[1st ele of list] = dict1[1st ele of list]

def newdict_by_extractingKeys(dict1, lst1):
    dict2= {}
    for i in range(len(lst1)):
        dict2[lst1[i]] = dict1[lst1[i]]
    print(dict2)    
# newdict_by_extractingKeys(sample_dict, keys)    

















               

