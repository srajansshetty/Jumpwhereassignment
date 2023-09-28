
sample_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}


ascending_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

descending_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))


print("Dictionary sorted in ascending order by value:", ascending_dict)
print("Dictionary sorted in descending order by value:", descending_dict)