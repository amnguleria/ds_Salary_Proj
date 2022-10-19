#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:14:24 2022

@author: amanguleria
"""

import pandas as pd

df=pd.read_csv('ds_Salary.csv')

de=df[df['Experience']=='EN']

dm=de[df['Employee_Location']=='IN']

dm.to_csv('cleaned_ds_salary',index=False)


