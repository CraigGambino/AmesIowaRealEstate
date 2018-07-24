import pandas as import pd
from collections import defaultdict


def drop_bad_columns(df, null_portion=(1/3)):
    df.drop([column for column in df.columns if df[column].isnull().mean() >= null_portion],
            axis=1,
            inplace=True)

def get_bad_columns(df, null_portion=(1/3)):
    return [column for column in df.columns if df[column].isnull().mean() >= null_portion]

def na_to_mode(data, column):
    modes = dict((column,data[column].mode()[0]) for column in data.columns)
    for column in data.columns:
        data[column].fillna(value=modes[column], inplace=True)

def mode_count(data, column):
    return sum((data[column] == data[column].mode()[0]).astype(int))

def null_groups(df):
    '''
    Args, df: pandas DataFrame
    Return, dict:
                keys are number of null entries
                values are lists of columns with
                the key-number of null values
    note: Only returns groups of 2 or more get_bad_columns
        with 1 or more null values in each column.
    '''
    # Get the number of null values in each column
    # in a dictionary as column:number
    temp = dict(df.isnull().sum())
    # Instantiate the defaultdict to hold lists
    # of columns with the same number of
    # null values
    dd = defaultdict(list)
    # Reverse the key and values from temp
    # and build out the list of column names
    # with each number of nulls
    for k,v in temp.items():
        dd[v].append(k)
    # filter the dictionary into groups in which
    # more than one column has at least 1 null
    dd = dict([(k,v) for k,v in dd.items() if k>0 and len(v)>1])
    # Finally, check that all of the group or none are null.
    return dict((key,val)
        for key,val in dd.items()
        if df[val]
            .isnull()
            .sum(axis=1)
            .value_counts()
            .index
            .tolist()
            == [0, len(val)] # ensures that all or none of the group are null
        )
    # Garbage collection: remove placeholder data structures
    del temp
    del dd
