"""
input: the test scores
initistes a iterator (counter) and accumlatoer (sum) and set it to zero 
loop through the list test scores
add alll the test scores
add all the te st scores
increment the counter by one
once the loop ends, there are no more scores to add 
divide the accumulator (sum By counter)
Output: print the average of the class scores. 

"""

"""
Scores
iterator, accumulator = 0
loop thourgh scores
    accumulator = accumlator + Scores
    iterator = iterator +1 
outpuy = accumulator / total score
print ouput
"""

def calculater_average(scores):
    iterator=0
    accumulator= 0
    student_count= len(scores)
    while iterator < len (scores):
        accumulator= accumulator + scores [iterator]
        iterator = iterator + 1
        average = accumulator /  student_count
    return average


    output = calculate_average(
        [50, 0, 100, 80, 90, 70, 50, 95, 60, 90, 54, 100, 70, 90])
    print("The average of total scores in the class is: ", output)
