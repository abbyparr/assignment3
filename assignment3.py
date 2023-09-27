import numpy as np

def NBAstats():
    filename = input("input file name")
    file = np.loadtxt("NBA_Player_Stats.tsv", dtype = float)
    print(file)
    
#determine:
    
    
    #field goal accuracy
        #FGM compared to FTA(made and attempted)
arrayF = np.array('FGM')
array2 = np.array('FTA')
comparison = arrayF == array2
two_arrays = comparison.all()
print(two_arrays)

    #three point accuracy
        #3PM compared to 3PA(made and attempted)
array3 = np.array('3PM')
array4 = np.array('3PA')
comparison = array3 == array4 
the_arrays = comparison.all()
print(the_arrays)

    #free throw accuracy
        #FTM compared to FTA(made and attempted)
arrayM = np.array('FTM')
arrayT = np.array('FTA')
comparison = arrayM == arrayT
compare_arrays = comparison.all()
print(compare_arrays)
    
    #average points scored per minute 
        #create array of points scored
arrayA = np.array(['PTS'])
np.sum(arrayA)
            #calculate average
avgpoints = np.average(arrayA)
print(avgpoints)
    

    #overall shooting accuracy 
arrayP = np.array('player')
accuracy = comparison.all()
print(accuracy)
    

    #average number of blocks per game 
        #create array of blocks per game
arrayB = np.array(['BLK'])
np.sum(arrayB)
            #calculate average
avgblocks = np.average(arrayB)
print(avgblocks)

    #average number of steals per game 
        #create array of steals per game
arrayS = np.array(['STL'])
np.sum(arrayS)
            #calculate average
avgsteals = np.average(arrayS)
print(avgsteals)

    
#create a list of the top 100 players and corresponding season with metrics
   
np.loadtxt('NBA_Player_Stats.tsv', dtype = 'float')

    #field goal accuracy
np.max(FGA, 'players', 100)
    #three point accuracy
np.max(3PA, 'players', 100)
    #free throw accuracy
np.max(FTA, 'players', 100)
    #average points scored per game
np.max(PTS, 'players',100)
    #overall shooting accuracy
np.max(players, 100)
    #average blocks per game
np.max(BLK, 'players', 100)
    #average steals per game
np.max(STL, 'players', 100)

#save each list as a separate file

with open('separatedata.txt', 'w'):
    np.savetxt('separatedata.txt')
    
    
