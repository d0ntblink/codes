#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print('Lebrons\'s total points scored between 2003 to 2013 is %s points' % sum(points))
# Print Average PPG
print('Lebron\'s avrage points per game is %0.1f points' %  (sum(points) / sum(games_played)))
# Print best scoring years (Ex: 2004/2005)
print('Lebron\'s best scorring season is %d/%d year' % ((2003 + points.index(max(points)),(2004 + points.index(max(points))))))
# Print worst scoring years (Ex: 2004/2005)
print('Lebron\'s worst scorring season is %d/%d year' % ((2003 + points.index(min(points)),(2004 + points.index(min(points))))))

'''the program is finding the index for his highest and lowest 
ever scored points in a year and adding to the start year wich is 2003/2004'''
