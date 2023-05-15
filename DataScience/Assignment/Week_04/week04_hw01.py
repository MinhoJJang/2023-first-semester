import featuretools as ft
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load data frames
loans = pd.read_csv("input/loans.csv")
clients = pd.read_csv("input/clients.csv")
payments = pd.read_csv("input/payments.csv")

# Create an entity set
es = ft.EntitySet(id='clients')
es = ft.EntitySet(id='loans')
es = ft.EntitySet(id='payments')

# Define entities
es = es.add_dataframe(
    dataframe_name='clients',
    dataframe=clients,
    index='client_id',
    time_index='joined'
)

es = es.add_dataframe(
    dataframe_name='loans',
    dataframe=loans,
    index='loan_id'
)

es = es.add_dataframe(
    dataframe_name='payments',
    dataframe=payments,
    index='payment_id',
    make_index=True,
    time_index='payment_date'
)

loan_rel = ft.Relationship(
    entityset=es,
    parent_dataframe_name='loans',
    parent_column_name='loan_id',
    child_dataframe_name='payments',
    child_column_name='loan_id'
)

# Define the relationship between the entities
new_rel = ft.Relationship(
    entityset=es,
    parent_dataframe_name='clients',
    parent_column_name='client_id',
    child_dataframe_name='loans',
    child_column_name='client_id'
)

stats = loans.groupby('client_id')['loan_amount'].agg(['mean','max','min'])
stats.columns = ['mean_loan_amount', 'max_loan_amount', 'min_loan_amount']

stats = clients.merge(stats, left_on='client_id', right_index=True, how='left')
stats.head(10)

print(stats)

es.add_relationship(
    relationship= new_rel
)

es.add_relationship(
    relationship= loan_rel
)

print(es)

print(es['payments'])

features, feature_names = ft.dfs(
    entityset=es,
    target_dataframe_name='clients',
    agg_primitives=['mean','max','percent_true','last'],
    trans_primitives=['year','month',]
)

features.to_csv("ft.csv")

# Create a new feature
feature_matrix, feature_defs = ft.dfs(
    entityset=es,

    target_dataframe_name='clients',
    agg_primitives=['sum'],
    trans_primitives=[],
    max_depth=1
)

# feature_matrix['total_loan_amount'] = feature_matrix['SUM(loans.loan_amount)']
#
# print(feature_matrix[['total_loan_amount']])
