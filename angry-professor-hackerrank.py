# Angry Professor Hackerrank

# A Discrete Mathematics professor has a class of students.
# Frustrated with their lack of discipline, the professor decides to cancel class 
# if fewer than some number of students are present when class starts.
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.


# if arrivedSturdents >= k: return 'NO'
# else: return 'YES'

def angryProfessor(k, a):
    onTime = 0
    for i in range(len(a)):
        if a[i] <= 0:
            onTime += 1
    if onTime >= k:
        return 'NO'
    else:
        return 'YES'
    

if __name__ == '__main__':
    print(angryProfessor(3, [-1, -3, 4, 2]))
