#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns

df = pd.read_csv(r'dataset/train.csv')
df.head()

df.info()

sns.factorplot('Sex', data=df, kind='count')

sns.factorplot('Pclass', data=df, kind='count')


def titanic_children(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex


df['person'] = df[['Age', 'Sex']].apply(titanic_children, axis=1)

sns.factorplot('Pclass', data=df, hue='person', kind='count')

df['Age'].mean()
