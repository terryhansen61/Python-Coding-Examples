import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("housing_data.csv")

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Year", y="Average_Home_Price",
                size="Interest_Rate", hue="Interest_Rate",
                palette="viridis", sizes=(20, 200),
                alpha=0.7)
sns.regplot(data=df,
            x="Year",
            y="Average_Home_Price",
            scatter=False,
            color="grey",
            line_kws={"linestyle":"--"})
plt.title("Housing Prices Over Time with Interest Rate Influence")
plt.xlabel("Year")
plt.ylabel("Average Home Price ($)")
plt.legend(title="Interest Rate (%)")
plt.show()


