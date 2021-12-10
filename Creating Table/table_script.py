from random import shuffle
to_append = []

str_1 = " sound_"
for i in range(1,15):
    to_append.append(str_1+str(i))

for i in range(42):
    to_append.append(" 111")

tablefilename = "search_table.txt"
tablefile = open(tablefilename, 'r')
tabletxt = tablefile.readlines()
tablefile.close()

print(len(tabletxt))
print(len(to_append))
outfilename = "search_table_1.txt"
outfile = open(outfilename, 'w')

print(to_append)
shuffle(to_append)
print(to_append)
if(len(tabletxt) == len(to_append)):
    for i in range(len(tabletxt)):
        line = tabletxt[i]
        end = line[-1]
        line = line[:-1]
        line = line + to_append[i] + end
        tabletxt[i] = line
else:
    print("***************** error *****************")

outfile.writelines(tabletxt)
outfile.close()
