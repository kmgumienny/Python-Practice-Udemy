# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than countin

string = "0123456789"
myIterator = iter(string)

for i in range(len(string)):
    print(next(myIterator))
