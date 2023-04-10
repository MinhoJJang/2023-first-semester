import featuretools as ft
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
# Create new entityset
es_clients = ft.EntitySet(id='clients')
es_loans = ft.EntitySet(id='loans')
es_payments = ft.EntitySet(id='payments')

loans = pd.read_csv("input/loans.csv")
clients = pd.read_csv("input/clients.csv")
payments = pd.read_csv("input/payments.csv")

# Create an entity from the client dataframe
# This dataframe already has an index and a time index
# index=RDB primary key
# time index= date_time feature

es_clients.add_dataframe(
    dataframe_name='clients',
    dataframe=clients,
    index='client_id',
    time_index='joined'
)

es_loans.add_dataframe(
    dataframe_name='loans',
    dataframe=loans,
    index='loan_id'
)

# es_clients.entity_from_datafrmaes(entity_id='clients',
#                                 dataframe=clients,
#                                 index='client_id',
#                                 time_index='joined')

# es_loans.entity_from_dataframe(entity_id='loans',
#                                dataframe=loans,
#                                index='loan_id')
#
# # Create an entity from the payments dataframe
# # This does not have an index
# es_payments.entity_from_dataframe(entity_id='payments',
#                                   dataframe=payments,
#                                   variable_types={'missed': ft.variable_types.Categorical},
#                                   make_index=True,
#                                   index='payment_id',
#                                   time_index='payment_date')


