#!/usr/bin/env python

import numpy as np
import pandas as pd

class Cleaner:
    df = pd.DataFrame()

    def __init__(self, df):
        self.df=df

    def dropna(self):
        self.df.dropna()

    def retdf(self):
        return self.df

    def desc(self):
        return self.df.describe()
