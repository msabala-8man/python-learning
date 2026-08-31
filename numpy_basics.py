import numpy as np

scores = np.array([72, 88, 91, 64, 55, 83, 77, 96, 69, 81])

total = np.sum(scores)
average = np.mean(scores)
minimum = np.min(scores)
maximum = np.max(scores)
standard_deviation = np.std(scores)

scores_80_or_more = scores[scores >= 80]
below_70 = scores[scores < 70]
between_70_and_90 = scores[(scores > 70) & (scores < 90)]

scores_plus_5 = scores + 5

print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard deviation:", standard_deviation)
print("Scores 80 or more:", scores_80_or_more)
print("Below 70:", below_70)
print("Between 70 and 90:", between_70_and_90)
print("Scores plus 5:", scores_plus_5)