from typing import List

scores: List[int] = []
newScores: List[int] = []
for i in range(5):

    a = input('enter your test score:')
    scores.append(int(a))
    if len(scores) == 5:
        print('all scores:' + str(scores))
        print('students with scores less than 60 will get 10 extra points')
for s in scores:
    if s >= 60:
        newScores.append(s)
    else:
        newScore = s + 10
        newScores.append(newScore)
print('all scores:' + str(newScores))
for n in range(len(newScores)):
    if newScores[n] != scores[n]:
        print('old score: {0} new score: {1}'.format(str(scores[n]), str(newScores[n])))
