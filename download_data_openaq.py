# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:25:55 2020

@author: Vinod
"""

import openaq
api = openaq.OpenAQ()

resp = api.cities(df=True, limit=10000)
idx = resp.query("country == 'IN'")
res = api.measurements(city='Delhi', parameter='pm25', limit=10000, df=True)
