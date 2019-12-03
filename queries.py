from config import period

queries = [
    {
        'Id': 'writerrdsmaxcpu',
        'MetricStat': {
            'Metric': {
                'Namespace': 'AWS/RDS',
                'MetricName': 'CPUUtilization',
                'Dimensions': [
                    {
                        'Name': 'DBClusterIdentifier',
                        'Value': 'somedbinstance'
                    },
                    {
                        'Name': 'Role',
                        'Value': 'WRITER'
                    },
                ]
            },
            'Period': period,
            'Stat': 'Maximum',
            'Unit': 'Percent'
        },
    },
    {
        'Id': 'readerrdsavgcpu',
        'MetricStat': {
            'Metric': {
                'Namespace': 'AWS/RDS',
                'MetricName': 'CPUUtilization',
                'Dimensions': [
                    {
                        'Name': 'DBClusterIdentifier',
                        'Value': 'somedbinstance'
                    },
                    {
                        'Name': 'Role',
                        'Value': 'READER'
                    },
                ]
            },
            'Period': period,
            'Stat': 'Average',
            'Unit': 'Percent'
        },
    },
    {
        'Id': 'kinesisincomingrecords',
        'MetricStat': {
            'Metric': {
                'Namespace': 'AWS/Kinesis',
                'MetricName': 'IncomingRecords',
                'Dimensions': [
                    {
                        'Name': 'StreamName',
                        'Value': 'somestream'
                    },
                ]
            },
            'Period': period,
            'Stat': 'Sum',
        }
    }
]
