# problem : to find the first reccuring element in a string
# example : i/p -> rahulbera o/p -> r

string = input()                # input string from user
elements = []                   # list for appending elements from the string
result   = []                   # list for all recurring elements

elements.append(string[0])      # appending the first element

for i in range(1,len(string)):          # iterating over the original string
    for j in range(len(elements)):      # iterating over the appended list
        if( string[i] == elements[j]):  # comparing with the current element of the string
            result.append(string[i])    # appending to list of all recurring elements
    elements.append(string[i])          # updating the elements list

print("first recurring element is : ",result[0])
