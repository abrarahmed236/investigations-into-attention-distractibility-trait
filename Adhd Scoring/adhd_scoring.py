from math import sqrt
import matplotlib.pyplot as plt

def correlation(x, y):
    # correlation calcualtion

    # x = recalls (repeat for x = f1)
    # y = adhd_scores
    # both need to be dictionaries with key as participant id
    # need to check if participant name is here by mistake.

    if(len(x)!= len(y)):
        print("func correlation: error, not supposed to happen, number of recalls and scores do not match")
        exit()

    N = len(x)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sq = 0
    sum_y_sq = 0

    for i in x:
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i]*y[i]
        sum_x_sq += x[i]*x[i]
        sum_y_sq += y[i]*y[i]

    correlation = ( N*sum_xy - sum_x*sum_y )
    correlation /= sqrt(( N*sum_x_sq - sum_x*sum_x )*( N*sum_y_sq - sum_y*sum_y ))
    
    return(correlation)

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
with open('data/data.csv') as f:
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

precisions = {}
recalls = {}
f1s = {}
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
    precisions[key] = precision
    recalls[key] = recall
    f1s[key] = f1
    #print(key, "p: ", precision, "r: ", recall, "f: ", f1, "ques: ", scores[key]) 

print("key\t\t\t\t\t    score\tprecision\trecall\t\tf1")
for i in scores:
    print("%s  %.4f\t%.4f\t\t%.4f\t\t%.4f"
          % (i, scores[i], precisions[i], recalls[i], f1s[i]))

print("\n\ncorrelation for recalls: ", correlation(recalls, scores))
print("r2: ", correlation(recalls, scores)*correlation(recalls, scores))
print("\n\ncorrelation for f1s: ", correlation(f1s, scores))
print("r2: ", correlation(f1s, scores)*correlation(f1s, scores))

"""
x = []
y = []
for key,value in scores.items():
    x.append(value)
    y.append(f1s[key])
plt.plot(x,y,'bo')
plt.xlabel("ADHD score")
plt.ylabel("F1 score")
plt.show()
"""

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

"""


"""
max_val = 0
min_val = 0
for line in scorecard:
    max_val += line[4]
    min_val += line[0]

print("max_val: ", max_val)
print("min_val: ", min_val)
"""


















