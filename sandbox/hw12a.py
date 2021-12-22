import os

import pandas as pd

def load_csv(name):
    path = f'{name}.csv'
    if not os.path.exists(path):
        from urllib.request import urlopen
        url = f'https://github.com/The-Japan-DataScientist-Society/100knocks-preprocess/raw/master/docker/work/data/{name}.csv'
        with urlopen(url) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
    return pd.read_csv(path)


def P001(df_receipt):
    return df_receipt.head(10)

def P002(df_receipt):
    columns = [
        'sales_ymd',  # 売上日
        'customer_id',  # 顧客 ID
        'product_cd',  # 商品コード
        'amount',  # 売上金額
    ]
    return df_receipt[columns].head(10)

def P003(df_receipt):
    columns = [
        'sales_ymd',  # 売上日
        'customer_id',  # 顧客 ID
        'product_cd',  # 商品コード
        'amount',  # 売上金額
    ]
    df = df_receipt[columns]
    df = df.rename(columns={'sales_ymd': 'sales_date'})
    df = df.head(10)
    return df

def P004(df_receipt):
    columns = [
        'sales_ymd',  # 売上日
        'customer_id',  # 顧客 ID
        'product_cd',  # 商品コード
        'amount',  # 売上金額
    ]
    df = df_receipt[columns]
    df = df[df['customer_id'] == 'CS018205000001']
    return df

def P005(df_receipt):
    columns = [
        'sales_ymd',  # 売上日
        'customer_id',  # 顧客 ID
        'product_cd',  # 商品コード
        'amount',  # 売上金額
    ]
    df = df_receipt[columns]
    df = df[df['customer_id'] == 'CS018205000001']
    df = df[df['amount'] >= 1000]
    return df

if __name__ == '__main__':
    df_receipt = load_csv('receipt')

    res = P001(df_receipt)
    print(res)

    res = P002(df_receipt)
    print(res)

    res = P003(df_receipt)
    print(res)

    res = P004(df_receipt)
    print(res)

    res = P005(df_receipt)
    print(res)
