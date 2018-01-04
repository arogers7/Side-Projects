"""
From a list of states and their number of electoral votes, I made a list that condenses the list based on duplicate number of votes.
Each member is formated [number of electoral votes for the entire state, number of states with this number of votes, number of states voting for the candidate]
The number of states voting for the candidate changes in every iteration, and is initialized to zero. For example, California is the only state with 55 votes so the list starts [[55,1,0]...]

In total there are 19 different number of electoral votes possible (condensed from the list of 50 states plus DC).

During the recursive permutations method, every combination of votes is created. Keep in mind that at this step, it's the number of states at a certain
The main thing to keep in mind is that in


"""
import math
#the following method was pulled from stackoverflow, credit to Mark Tolonen
def nCr(n,r):

    f = math.factorial
    return f(n) / f(r) / f(n-r)

#this list allows a count of the number of successful combinations to be accessed
#from objects within the program.
imp_var = {'is_270':0}
def calc_number_of_combos(electoral_college):
    total = 1
    for state in electoral_college:
        total *= nCr(state[1],state[2])
    imp_var['is_270'] += total
def recursive_permutations(electoral_college,sum,index):
    """

    """
    target = 270
    max_index = 19
    if sum == target:
        calc_number_of_combos(electoral_college)
        print(imp_var['is_270'])
    elif sum < target and index < max_index:
        num_votes = electoral_college[index][0]
        num_of_duplicates = electoral_college[index][1]
        #this calls this method recursively for the case where none of the states
        #this the number of votes in question vote for the candidate.
        recursive_permutations(electoral_college,sum,index+1)
        #this calculates what the sum would be if any number of the states with
        #the given weight were to vote for the candidate
        for i in range(1,num_of_duplicates+1):
            #a copy of the electoral college is made so that changes in one call do not affect changes in another call
            new_electoral_college = electoral_college.copy()
            #this saves the number of states that choose the candidate for later calculations
            new_electoral_college[index][2] = i
            #the new sum of votes for the candidate are calculated
            recursive_permutations(new_electoral_college,sum+num_votes*i,index+1)
if __name__ == '__main__':
    #this is a list of lists where the first index is the number of electoral votes,
    #the second index is the number of states with those votes, and
    #the third index is the number of states that use
    electoral_college = [[55, 1, 0], [38, 1, 0], [29, 2, 0], [20, 2, 0], [18, 1, 0], [16, 2, 0], [15, 1, 0], [14, 1, 0], [13, 1, 0], [12, 1, 0], [11, 4, 0], [10, 4, 0], [9, 3, 0], [8, 2, 0], [7, 3, 0], [6, 6, 0], [5, 3, 0], [4, 5, 0], [3, 8, 0]]

    recursive_permutations(electoral_college,0,0)
    print('the program is completed, the total number of combinations is',imp_var['is_270'])
    #the answer I got was 16,973,726,193,241
