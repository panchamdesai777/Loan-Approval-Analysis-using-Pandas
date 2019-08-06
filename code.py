import numpy as np
import pandas as pd
from scipy.stats import mode 

#Load the dataset
bank=pd.read_csv(path) 

#Create the variable 'categorical_var' to check all categorical values
categorical_var= bank.select_dtypes(include = 'object')
print(categorical_var)

#Create the variable 'numerical_var'
numerical_var = bank.select_dtypes(include = 'number')
print (numerical_var)

# load the dataset and drop the Loan_ID
banks= bank.drop(columns='Loan_ID')


# check  all the missing values filled.

print(banks.isnull().sum())

# apply mode 

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.

print(banks.isnull().sum())


# check the avg_loan_amount
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)


# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

#convert Loan_Amount_Term which is in months to year and store the result in a variable 'loan_term'.
loan_term = banks["Loan_Amount_Term"].apply(lambda x: int(x) / 12)
print('x:',loan_term)
print("="*30)

#Find the number of applicants having loan amount term greater than or equal to 25 years and store them in a variable called 
big_loan_term = len(banks[banks["Loan_Amount_Term"]>=300])
print(big_loan_term)


#check the average income of an applicant and the average loan given to a person based on their income.

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)


