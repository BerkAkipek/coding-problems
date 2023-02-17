# Climbing the LeaderBoard

# An arcade game player wants to climb to the top of the leaderboard and track their ranking.
# The game uses Dense Ranking, so its leaderboard works like this:
# 1. The player with the highest score is ranked number  on the leaderboard.
# 2. Players who have equal scores receive the same ranking number, 
# and the next player(s) receive the immediately following ranking number.

# Lets create a Dense Ranking function. 

def denseRanking(ranked):
    position = 1
    leaderBoard = [position]
    first = ranked[0]
    for i in range(1, len(ranked)):
        if first > ranked[i]:
            first = ranked[i]
            position += 1
            leaderBoard.append(position)
        else:
            leaderBoard.append(position)
    return leaderBoard


# Solution 

def climbingLeaderboard(ranked, player):
    # Write your code here
    unique_rank = sorted(list(set(ranked)), reverse=True)

    rank_result = []
    for score in player:
        while len(unique_rank) > 0 and score >= unique_rank[-1]:
            unique_rank.pop()

        rank_result.append(len(unique_rank) + 1)
    
    return rank_result


if __name__ == '__main__':
    print(denseRanking([100, 100, 50, 40, 40, 20, 10]))