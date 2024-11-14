import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    "/Users/rudolphstockenstrom/Documents/Data projects/P2 - Destricptive Statistics/us_data.csv"
)

# print(data.head())

# Check for missing values
# print(data.isnull().sum())

# Fill or drop missing values if necessary
# data = data.dropna()  # Or use data.fillna() to fill with specific values

# Display data types and basic info
# print(data.info())

stats = data.describe()
print(stats)

sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="year", y="firms", marker="o", label="Firms")
plt.title("Growth of Firms in America (1978-2022)")
plt.xlabel("Year")
plt.ylabel("Number of Firms")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="year", y="job_creation", marker="o", label="Job Creation")
plt.title("Job Creation in America (1978-2022)")
plt.xlabel("Year")
plt.ylabel("Number of Jobs Created")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate growth rates
data["firms_growth_rate"] = data["firms"].pct_change() * 100
data["job_creation_growth_rate"] = data["job_creation"].pct_change() * 100

# Descriptive statistics for growth rates
growth_stats = data[["firms_growth_rate", "job_creation_growth_rate"]].describe()

# Display the growth statistics
print(growth_stats)

# Plotting growth rates
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=data, x="year", y="firms_growth_rate", marker="o", label="Firms Growth Rate"
)
sns.lineplot(
    data=data,
    x="year",
    y="job_creation_growth_rate",
    marker="o",
    label="Job Creation Growth Rate",
)
plt.title("Growth Rates of Firms and Job Creation in America (1978-2022)")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
