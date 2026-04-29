import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("w4/data/housing.csv")

# Show full data
print("Full Data:")
print(df)

# Filter data (Price > 400000)
filtered = df[df["Price"] > 400000]

print("\nFiltered Data (Price > 400000):")
print(filtered)

# Plot graph
plt.bar(df["City"], df["Price"])

plt.title("City vs Price")
plt.xlabel("City")
plt.ylabel("Price")

plt.show()

# Basic analysis
print("\nMaximum Price:", df["Price"].max())
print("Minimum Price:", df["Price"].min())
print("Average Price:", df["Price"].mean())