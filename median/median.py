D8 = { 'Italy': 17,
       'UK': 39,
       'USA': 29,
       'Germany': 16,
       'France': 8,
       'China': 3,
       'Romania': 1,
       'South Korea': 5,
       'Netherlands': 3,
       'Japan': 15,
       'Russia': 3,
       'Australia': 1,
       'Sweden': 3,
       'Taiwan': 1,
       'India': 2,
       'Switzerland': 1,
       'Malaysia': 1,
       'Spain': 1,
       'Czech Republic': 2,
       'Austria': 1,
       'Serbia': 1,
       'Ukraine': 1,
       'Denmark': 1 }

# values = D8.values()
# print(values)

value = []
for key in D8.keys() :
    value.append(D8[key])

numbers = len(value)
value.sort()

if numbers % 2 == 0:
    median1 = value[numbers // 2]
    median2 = value[numbers // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = value[numbers // 2]
print("Median is: " + str(median))