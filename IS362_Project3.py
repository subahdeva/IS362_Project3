#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import sqlalchemy as sqla
from sqlalchemy import create_engine

sql = '''
SELECT Customer.Lastname, Customer.FirstName, Track.name, Album.title
FROM Customer
    JOIN INVOICE
        ON Customer.CustomerId = Invoice.CustomerId
    JOIN InvoiceLine
        ON Invoice.InvoiceId = InvoiceLine.InvoiceId
    JOIN Track
        ON InvoiceLine.TrackId = Track.TrackId
    JOIN ALBUM
        ON Track.AlbumId = Album.AlbumId
ORDER BY Customer.LastName, Customer.FirstName, Track.name, Album.title'''

db = sqla.create_engine('sqlite:///Chinook.sqlite')
pd.read_sql(sql, db).head(5)


# In[ ]:




