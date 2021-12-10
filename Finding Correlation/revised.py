filelines = []
with open('data/data.csv') as f:
    for line in f.readlines():
        filelines.append(line)

filelines = filelines[1:]


scores1 = 0
scores2 = 0
print('individual average reaction times: ')
for line in filelines:
    participant = line.split(',')[0]
    file1 = line.split(',')[19]
    file2 = line.split(',')[20]
    #print(participant, file1, file2)
    counter1 = 0
    score1 = 0
    counter2 = 0
    score2 = 0
    with open('data/'+file1) as f:
        for line in f.readlines():
            score1 += int(line.split()[-1])
            counter1 += 1
    
    with open('data/'+file2) as f:
        for line in f.readlines():
            score2 += int(line.split()[-1])
            counter2 += 1

    scores1 += score1/counter1
    scores2 += score2/counter2
#    print('without: ', score1/counter1, ' with: ', score2/counter2)
    print('without: %.4f\twith: %.4f' % (score1/counter1, score2/counter2) )

print('\n total average:')  
print('without: %.4f' % (scores1/12))
print('with:    %.4f' % (scores2/12))

