import featuretools as ft
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Load data frames
loans = pd.read_csv("input/loans.csv")
clients = pd.read_csv("input/clients.csv")

# Create an entity set
es = ft.EntitySet(id='clients')
es = ft.EntitySet(id='loans')

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

# Define the relationship between the entities
new_rel = ft.Relationship(
    entityset=es,
    parent_dataframe_name='clients',
    parent_column_name='client_id',
    child_dataframe_name='loans',
    child_column_name='client_id'
)
es.add_relationship(
    relationship= new_rel
)

# Create a new feature
feature_matrix, feature_defs = ft.dfs(
    entityset=es,
    target_dataframe_name='clients',
    agg_primitives=['sum'],
    trans_primitives=[],
    max_depth=1
)

feature_matrix['total_loan_amount'] = feature_matrix['SUM(loans.loan_amount)']

print(feature_matrix[['total_loan_amount']])