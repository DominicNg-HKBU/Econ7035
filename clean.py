# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:23:26 2024

@author: dominic.ng  Student No 22462244

Assumption: the headers of both CSV files will not be changed
"""

import pandas as pd


def clean(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, how='left', left_on='respondent_id', right_on='id').drop(['id'], axis=1)
    merged_df.dropna(inplace=True)
    filter_result=merged_df['job'].str.contains(pat = 'nsurance')
    merged_df=merged_df[~filter_result]
    #merged_df.to_csv("respondent_cleaned.csv",index=False)
    return merged_df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Respondent Contact (CSV) File NAme')
    parser.add_argument('input2', help='Respondent Other (CSV) File Name')
    parser.add_argument('output', help='Respondent Cleaned (CSV) File Name')
    args = parser.parse_args()

    cleaned_df = clean(args.input1, args.input2)
    cleaned_df.to_csv(args.output, index=False)