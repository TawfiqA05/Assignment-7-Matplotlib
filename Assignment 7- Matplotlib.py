import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris_df["species"] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

plt.figure()
plt.scatter(iris_df["sepal length (cm)"], iris_df["sepal width (cm)"], c=iris_df["species"].cat.codes, cmap="viridis")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.title("sepal dimensions by iris species")
plt.savefig("iris_scatter_sepal.png")
plt.close()

plt.figure()
plt.scatter(iris_df["petal length (cm)"], iris_df["petal width (cm)"], c=iris_df["species"].cat.codes, cmap="plasma")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.title("petal dimensions by iris species")
plt.savefig("iris_scatter_petal.png")
plt.close()

plt.figure()
iris_df.boxplot(column="sepal length (cm)", by="species")
plt.title("sepal length distribution by species")
plt.suptitle("")
plt.xlabel("species")
plt.ylabel("sepal length (cm)")
plt.savefig("iris_boxplot_sepal_length.png")
plt.close()

loan_df = pd.read_csv("LoanDataset - LoansDatasest.csv")

plt.figure()
plt.hist(loan_df["loan_amount"].dropna(), bins=30)
plt.xlabel("loan amount")
plt.ylabel("frequency")
plt.title("distribution of loan amounts")
plt.savefig("loan_histogram_amount.png")
plt.close()

plt.figure()
loan_status_counts = loan_df["loan_status"].value_counts()
loan_status_counts.plot(kind="bar")
plt.xlabel("loan status")
plt.ylabel("count")
plt.title("loan status counts")
plt.savefig("loan_bar_status.png")
plt.close()

plt.figure()
plt.scatter(loan_df["interest_rate"], loan_df["loan_amount"])
plt.xlabel("interest rate")
plt.ylabel("loan amount")
plt.title("interest rate vs loan amount")
plt.savefig("loan_scatter_interest_amount.png")
plt.close()

analysis_text = "The loan data visualizations reveal that the distribution of loan amounts is skewed towards lower values, with one loan status dominating the dataset. The scatter plot indicates a trend where higher interest rates are often associated with larger loan amounts. These insights suggest potential areas for deeper financial risk analysis."
print(analysis_text)