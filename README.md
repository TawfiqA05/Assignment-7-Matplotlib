# Assignment-7-Matplotlib

## Project Purpose
This project demonstrates data visualization using Python and Matplotlib with real-world data. It includes visual analysis of Fisher's Iris data and loan data extracted from a CSV file to uncover insights and trends.

## Project Structure
- **Iris Data Visualizations:**
  - A scatter plot of sepal dimensions by iris species.
  - A scatter plot of petal dimensions by iris species.
  - A boxplot showing the distribution of sepal lengths by species.
- **Loan Data Visualizations:**
  - A histogram displaying the distribution of loan amounts.
  - A bar plot showing counts of different loan statuses.
  - A scatter plot comparing interest rates with loan amounts.
- **Analysis:**
  - A printed paragraph summarizing insights from the loan data visualizations.

## Implementation Details
- The Iris dataset is loaded using scikit-learn and converted into a pandas DataFrame.
- The loan data is loaded from the CSV file `LoanDataset - LoansDatasest.csv`.
- All visualizations are generated using Matplotlib and saved as PNG files.
- Variables are in snake_case and the code is organized in a single script.

## Limitations
- The script does not include extensive error handling.
- Data quality issues in the loan data are not explicitly managed.
- The visualizations are basic and may be further improved for aesthetics.
