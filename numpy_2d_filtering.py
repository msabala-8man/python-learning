import numpy as np

# TOPIC:
# NumPy: 2D Arrays Filtering and Conditions
#
# - boolean conditions
# - filtering
# - multiple conditions
# - 2D arrays


scores = np.array([
    [72, 88, 91, 64, 55],
    [83, 76, 95, 68, 71],
    [59, 87, 79, 92, 66],
    [81, 73, 54, 89, 97]
])


# EXERCISE:
#
# 1. Print all scores greater than or equal to 80.
# 2. Print all scores below 70.
# 3. Print all scores between 70 and 90.
# 4. Print all scores greater than 90 OR below 60.
# 5. Count how many scores are greater than or equal to 80.
# 6. Count how many scores are below 70.
# 7. Add 5 points to every score.
# 8. Add 10 points only to scores below 70.
# 9. Replace every score below 60 with 60.
# 10. Calculate the average of scores greater than or equal to 80.

print(scores[scores >= 80])                     # 1.
print(scores[scores < 70])                      # 2.
print(scores[(scores > 70) & (scores < 90)])    # 3.
print(scores[(scores > 90) | (scores < 60)])    # 4.
print(len(scores[scores >= 80]))                # 5.
print(len(scores[scores < 70]))                 # 6.
print(scores + 5)                               # 7.
scores[scores < 70] += 10                       # 8.
scores[scores < 60] = 60                        # 9.
print(np.mean(scores[scores >= 80]))            # 10.  
