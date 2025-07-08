import matplotlib.pyplot as plt

# ডেটা
parties = ['A', 'B', 'C', 'D']
votes = [13, 6, 5, 6]

# বার চার্ট আঁকা
plt.bar(parties, votes, color=['green', 'blue', 'orange', 'red'])
plt.title("Political Party Popularity")
plt.xlabel("Parties")
plt.ylabel("Number of People")
plt.show()
