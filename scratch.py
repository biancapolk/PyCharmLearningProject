words = 'one', 'two', 'three', 'four'
outF = open("myOutFile1.txt", "w+")
outF.write("Number of words: {}".format(len(words)))
outF.close()
