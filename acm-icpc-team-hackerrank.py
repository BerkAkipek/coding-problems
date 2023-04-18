#!/usr/bin/python3

# ACM ICPC Team Hackerrank

# There are a number of people who will be attending ACM-ICPC World Finals.
# Each of them may be well versed in a number of topics.
# Given a list of topics known by each attendee, presented as binary strings, determine the maximum number of topics a 2-person team can know.
# Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not.
# Also determine the number of teams that know the maximum number of topics.
# Return an integer array with two elements.
# The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.

# Example
# n = 3
# topics = ['10101', '11110', '00010']

# For clarity columns are alligned below
# 10101
# 11110
# 00010

# TThese are all possible teams that can be formed:

# Members Subjects
# (1,2)   [1,2,3,4,5]
# (1,3)   [1,3,4,5]
# (2,3)   [1,2,3,4]

# In this case, the first team will know all 5 subjects.
# hey are the only team that can be created that knows that many subjects, so [5, 1] is returned.

test_case01 = ['10101', '11100', '11010', '00101']
test_case02 = ['11101', '10101', '11001', '10111', '10000', '01110']

def knowledge_check(member1, member2):
    num_known = 0
    for i, j in zip(member1, member2):
        if i == '1' or j == '1':
            num_known += 1
    return num_known


def acmTeam(topic):
    max_topics, num_max_teams = 0, 0
    for i in range(len(topic) - 1):
        for j in range(i+1, len(topic)):
            topics_known = knowledge_check(topic[i], topic[j])
            if topics_known > max_topics:
                max_topics = topics_known
                num_max_teams = 1
            elif topics_known == max_topics:
                num_max_teams += 1
    return [max_topics, num_max_teams]

topics = ['10101', '11110', '00010']
print(acmTeam(topics))
