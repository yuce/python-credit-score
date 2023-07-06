import pickle
from typing import Tuple
import os

import numpy as np
from hazelcast.db import connect
from hazelcast import HazelcastClient

from clc import client_config
client_config.statistics_enabled = False
conn = connect(client_config)
client = HazelcastClient(client_config)

with open(os.path.dirname(__file__) + "/model.pickle", "rb") as f:
    model = pickle.load(f)

QUERY = '''
    SELECT
        Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, 
        Num_Credit_Card, Interest_Rate, Num_of_Loan,
        Avg_Num_of_Days_Delayed, Num_of_Delayed_Payment, Credit_Mix,
        Outstanding_Debt, Credit_History_Age, Monthly_Balance
    FROM customer
    WHERE __key = ?
'''

def transform(item: Tuple[str, dict]) -> Tuple[str, str]:
    customer_id, _ = item
    with conn.cursor() as cursor:
        cursor.execute(QUERY, (customer_id,))
        row = cursor.fetchone()
        features = np.array([row])
        result = model.predict(features)[0]
        return customer_id, result
