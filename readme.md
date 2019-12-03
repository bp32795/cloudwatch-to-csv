# cloudwatch-to-csv

A python tool that converts AWS CloudWatch metrics into a csv format.

## Getting Started

You will need python 3.6 for this to run. This may run on other versions of python, but was created with 3.6.

`git clone` this repository to your local drive.

`cd` into the main folder.

Run `pip install -r requirements.txt` to install all necessary python libraries.

## Configure and Run

1. Edit `config.py` with the date range and period you want data for. Edit `queries.py` with the data you want to scrape. Examples are currently in both files.

   You will need AWS credentials in your .aws directory or an equivalent method of authentication to AWS. This script will not provide authentication.

    Also, keep in mind that AWS will only have data for certain date ranges and periods by default (for example, up to 1s period or the last two weeks), so make sure your config.py will have data to scrape. 

2. Run `cloudwatch-to-csv.py`

The results will output to a `results` directory in the root directory.

## Built With

* [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data) - AWS Library. Link contains query syntax.
* [Pandas](https://pandas.pydata.org/) - Dataframe Management

## Contributing

There is lots of oppurtunity to improve this tool. Please feel free to submit pull requests, and I will review them ASAP.

## Issues

Please open any issues that you have running the tool or following documnentation. If the results return empty, make sure that there is data showing up on cloudwatch first, and that there is data for the selected range and period combination

## Authors

* **[Brandon Menke](https://www.linkedin.com/in/brandonmenke/)** - *Initial work* 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
