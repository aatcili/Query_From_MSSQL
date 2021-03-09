# %%
import pandas as pd
import pyodbc
import numpy as np
import matplotlib.pyplot as plt

connstring = "Driver={SQL Server Native Client 11.0};"
                      "Server=server_name;"
                      "Database=db_name;"
                      "Trusted_Connection=yes"
conn = pyodbc.connect(connstring)

query = "SELECT * FROM Table"

df = pd.read_sql(query, conn)

df