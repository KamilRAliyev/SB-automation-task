import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_plot(df):
    df = df.sort_values(by='date')
    x = np.arange(0,len(df))
    fig, ax = plt.subplots(1, figsize=(12,6))
    for idx, val in df.iterrows():
        color = '#2CA453'
        if val['open'] > val['close']: color= '#F04730'
        plt.plot([x[idx], x[idx]], 
                 [val['low'], val['high']], 
                 color=color)
        plt.plot([x[idx], x[idx]-0.1], 
                 [val['open'], val['open']], 
                 color=color)
        plt.plot([x[idx], x[idx]+0.1], 
                 [val['close'], val['close']], 
                 color=color)

    plt.xticks(x[::10], df.date.dt.date[::10])
    return plt

def get_data_frame(file_path="./outputs/gathered_data.csv", stock_name="AAPL"):
    df = pd.read_csv(file_path)

    df_stock = df[df['stock name'] == stock_name].copy()
    df_stock['date'] = pd.to_datetime(df_stock['date'])
    
    df_stock.reset_index(inplace=True)
    return df_stock

def save_plot(plt, file_path="./outputs/plot/plot.png"):
    plt.savefig(file_path)
    return file_path


def get_report_data(df):
    # I don't know how to calculate these values. But I will try...
    ## If (close - open) is big then best stock day
    #  else then worst stock day
    df_sorted = df.assign(f = df['close'] - df['open']).sort_values('f')     
    return {
    "best_stock_day": df_sorted.iloc[-1]['date'],
    "worst_stock_day": df_sorted.iloc[0]['date'],
    "stored_data_len": len(df)
    }