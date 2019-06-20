# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.

ipAddress = input("Please enter an IP address ")
printText = ''
numNumbers = 0
numSegment = 1

for i in range(0,  len(ipAddress)):
    if ipAddress[i] in '0123456789':
        numNumbers += 1
    elif ipAddress[i] == '.':
        printText += 'Segment {} has a length of {}. '.format(numSegment, numNumbers)
        numSegment += 1
        numNumbers = 0
    if i == len(ipAddress) - 1:
        printText += 'Segment {} has a length of {}. '.format(numSegment, numNumbers)


print(printText)
