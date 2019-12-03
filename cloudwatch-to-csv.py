import boto3
import pandas as pd
from config import startTime,endTime,period
from queries_test import queries
import os

def cloudwatch_scraper(startTime,endtime,queries):
    client = boto3.client('cloudwatch')
    response = client.get_metric_data(
        MetricDataQueries=queries,
        StartTime=startTime,
        EndTime=endtime,
    )

    results = response['MetricDataResults']

    df = pd.DataFrame(columns=['time'])

    data = results[0]
    timestamps = data['Timestamps']
    df['time'] = timestamps
    for data in results:
        id = data['Id']
        temp_df=pd.DataFrame(columns=['time',id])
        temp_df[id]= data['Values']
        temp_df['time'] = data['Timestamps']

        df = df.merge(temp_df,how='outer',on='time')

    df['time']=df['time'].astype(str).str[:-6]
    df['time']=pd.to_datetime(df['time'])
    df=df.fillna(0)
    return df


def checkDir():
    outdir = './results'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
def main():
    df = cloudwatch_scraper(startTime, endTime, queries)
    checkDir()
    df.to_csv("results/cloudwatch-data-from-{}{}{}-to-{}{}{}-period-{}.csv".format(
        startTime.date().year,
        startTime.date().month,
        startTime.date().day,
        endTime.date().year,
        endTime.date().month,
        endTime.date().day,
        period),index=False)

if __name__ == '__main__':
    main()



