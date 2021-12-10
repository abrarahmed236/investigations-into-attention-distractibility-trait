items = [0,0,0,0,0 ]
scorecard = [
    [-1,0,1,2,3],
    [-1,0,1,2,3],
    [-1,0,1,2,3],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-1,0,1,2,3],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-1,0,1,2,3],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-2,-1,0,1,2],
    [-1,0,1,2,3],
    [-2,-1,0,1,2],
    [-1,0,1,2,3],
    ]

lines = []
with open('data.csv') as f:
    for line in f.readlines():
        lines.append(line)

participants = {}
remember = {}
scores = {}
for line in lines[1:]:
    values = line.split(',')[0:19]
    remember[values[0]] = line.split(',')[21:49]
    participants[values[0]] = values[1:]

for key, value in participants.items():
    score = 0
    for i, v in enumerate(value):
        score += int(scorecard[i][int(v)-1])
    scores[key] = score



for key, value in remember.items():
    #print(key, ": ", value)
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i, v in enumerate(value):
        if i < 14:
            if int(v) == 1:
                tp += 1
            else:
                fn += 1
        else:
            if int(v) == 1:
                fp += 1
            else:
                tn += 1
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*precision*recall/(precision+recall)
    print(key, "p: ", precision, "r: ", recall, "f: ", f1, "ques: ", scores[key]) 
                



"""    
for key, value in participants.items():
    score = 0
    for i, v in enumerate(value):
        score += int(scorecard[i][int(v)-1])
#   print(key, ": ", score)
#    for i in range(len(value)):
#        print(i+1, ": ", value[i])
    print(value)
    print()


max_val = 0
min_val = 0
for line in scorecard:
    max_val += line[4]
    min_val += line[0]

print("max_val: ", max_val)
print("min_val: ", min_val)
"""

"""
# correlation calcualtion

# x = recalls (repeat for x = f1)
# y = adhd_scores

if(len(x)!= len(y))
    print("error, fuck off!! this wasn't supposed to happen, you suck")
    print("get your shit together you teaspoon!!")
    exit()

N = len(x)
sum_x = 0
sum_y = 0
sum_xy = 0
sum_x_sq = 0
sum_y_sq = 0

for i in range(N):
    sum_x += x[i]
    sum_y += y[i]
    sum_xy += x[i]*y[i]
    sum_x_sq += x[i]*x[i]
    sum_y_sq += y[i]*y[i]

correlation = ( N*sum_xy - sum_x*sum_y )
correlation /= sqrt(( N*sum_x_sq - sum_x*sum_x )*( N*sum_y_sq - sum_y*sum_y ))
print("correlation: ", correlation)



"""





















