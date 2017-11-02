inputValues = [1, 2, 3, 5, 6, 7]
inputValues = [1, 2, 2, 0, 2, 0]
inputValues = [0, 0, 0, 6, 7, 8]

inputValues.sort()

print("initial values" + str(inputValues))

# reject = 0
# for idx, val in enumerate(inputValues):
#     if val > 5:
#         reject += 1

# if reject >2:
#     print('not possible')
#     exit(0)

for idx, val in enumerate(inputValues):

    if inputValues[0] == 0 and inputValues[1] == 0:
        inputValues.remove(0)
        inputValues.append(0)
        print(inputValues)
print(inputValues)

hour = '{0}{1}'.format(str(inputValues[0]), str(inputValues[1]))
inputValues.pop(0)
inputValues.pop(0)

inputValues.sort()
print('hour: '+ str(hour))

print(inputValues)
for idx, val in enumerate(inputValues):
    if val > 5:
        print(inputValues)

min = '{0}{1}'.format(str(inputValues[0]), str(inputValues[1]))
inputValues.pop(0)
inputValues.pop(0)

print(inputValues)



sec = '{0}{1}'.format(str(inputValues[2]), str(inputValues[3]))

print('{}:{}:{}'.format(hour, min, sec))

# hour small
# hour <24
# max one 0 in each place
# hour 1-23
# min 1-59
# sec 1-59
