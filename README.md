
# Loan Prediction Project

Welcome to the Loan Prediction Project repository! This project focuses on predicting loan approval using machine learning techniques, Big Data, AI, and Android development. Below is an overview of the dataset, Python files, and expected output.

## Dataset

The dataset used in this project is included in the `/data` directory. It consists of historical data with various attributes related to loan applications. The dataset is divided into training and testing sets, allowing for robust model training and evaluation.

[DataSet](https://github.com/KhushalKhare/Loan-Prediction/blob/main/Loan-Prediction.csv): Contains data used to train machine learning models

Feel free to explore the datasets and refer to the project documentation for a detailed description of each attribute.

## Python Files

[Jupyter Notebook](https://github.com/KhushalKhare/Loan-Prediction/blob/main/Loan%20Prediction.ipynb)
[ML Tool](https://github.com/KhushalKhare/Loan-Prediction/blob/main/MLTools.py)

Explore these files to gain insights into the project's implementation.

## Data & Method

We had trained different machine learning models to predict the likelihood of loan repayment for a dataset of historical loan applications. The dataset includes information about loan applicants, such as their credit history, income, education, employment, and loan amount.

The dataset consists of 614 rows and 13 columns. We pre-processed the data to handle missing values, outliers, and inconsistencies. We then split the data into training and testing datasets in the ratio of (80:20). The training dataset was used to develop and train the machine learning models, while the testing dataset was used to evaluate the model’s performance.

We have trained three different machine learning models: K-nearest neighbours (KNN), decision trees, and random forests and compared the performance of each model on the testing set using precision.

Precision is a measure of how well a model can identify positive cases, which in this case are loans that are likely to be repaid. The highest accuracy was achieved by the random forest, with a value of 0.81 followed by decision tree and KNN with a value of 0.80. This means that the random forest model was able to correctly identify 81% of the loans that were likely to be repaid

## Output

Upon successful execution of the project, you can expect the following outcomes:

The best performing model was the random forest classifier with an accuracy of 86.1% on the training set and 84.0% on the testing set. The model also achieved a recall score of 84.3% for the positive class (loans that were not repaid).

The following table summarises the results of the random forest classifier model on the training and testing sets:

The model has correctly predicted 478 out of 500 loan applications that were not repaid, and 183 out of 200 loan applications that were repaid.

Overall, the above results draw a conclusion that a random forest classifier can be used to accurately predict loan repayment.

## Conclusion

The findings of this study have significant implications for the financial industry. By adopting machine learning-powered loan prediction systems, financial institutions can:

● Enhance loan approval decision-making, reducing risk and improving profitability

● Personalise loan offerings based on individual borrower risk profiles

● Improve customer satisfaction by providing more informed and timely loan decisions

● Optimise resource allocation and streamline loan processing operations

This study demonstrates the effectiveness of machine learning in accurately predicting loan repayment behaviours. The developed model can be readily integrated into lending platforms to automate loan approval decisions and enhance risk assessment capabilities. Financial institutions can leverage these advancements to make informed lending decisions, improve customer experience, and strengthen their financial footing.
