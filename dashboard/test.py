subsDict = {}
with open('dashboard\subreddits.txt') as myfile:
    for line in myfile:
        name, description = line.partition("=")[::2]
        subsDict[name.strip()] = description.strip()
supportSubs = list(subsDict.keys())
for i in range(len(supportSubs)):
    supportSubs[i] = supportSubs[i][2:]
print(supportSubs)