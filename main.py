#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import websockets
import json
import pandas as pd
import asyncio
import ta

api_key = "qXrjNB7Vr00oOeCSiOHnEnwqVZGcLbcJrMPdetpxbc62EAX6ua3FusB4hnOlxPbY"
api_secret = "Szp0eXA3Djy8hicxnHzKNSBOQ5FiUskqXA2gDIedvKLap2V57CaGf2QU03gTYVY8"
from binance.client import Client


# In[3]:


stream = websockets.connect('wss://testnet.binance.vision/stream?streams=adausdt@miniTicker')


# In[4]:


def createframe(msg):
  df = pd.DataFrame([msg])
  df = df.loc[:,['s', 'E', 'c']]
  df.columns = ['symbole', 'Time', 'Price']
  df.Price = df.Price.astype('float')
  df.Time = pd.to_datetime(df.Time, unit='ms')
  return df


# In[5]:

async def main():
  async with stream as receiver:
      while True:
        data = await receiver.recv()
        data = json.loads(data)['data']
        df = createframe(data)
        print(df)


# In[6]:
if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())



