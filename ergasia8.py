from random import randint

numbers = [randint(-30,30) for x in range(30)]
found_triplet = False


for i in range(0, len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
                       if(numbers[i] + numbers[j] + numbers[k] == 0):
                           print(numbers[i], numbers[j], numbers[k])
                           found_triplet = True
if(found_triplet == False):
    print "No triplets"