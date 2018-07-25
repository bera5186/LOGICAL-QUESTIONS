# problem : find the lenght of largest substring in which all letters are vowel
# example : i/p -> abbauic , o/p -> 3 as 'aui' is the largest substring in which
#           all letters are vowel 
s = input()
lenght = 0        # lenght counter
frequency = []    # frequency counter
lenghts = []      # list containing lenghts at all stages


# for counting frequency
for i in range(len(s)):
    if s[i] in ('a','e','i','o','u'):
        frequency.append(1)
    else :
        frequency.append(0)

# for finding lenghts
for i in range(len(frequency)):
    if(frequency[i] == 1):
        lenght = lenght + 1
    else :
        lenght = 0
    lenghts.append(lenght)

# maximum lenght   
print(max(lenghts))
