import boto3
import pandas as pd

#código para interação com AWS S3

s3_client = boto3.client('s3')

s3_client.download_file("m.rodrigo18-bucket-igti", 
                        "data/enem2019.csv",
                        "data/enem2019.csv")

df = pd.read_csv("data/enem2019.csv", sep=";")
print(df)

s3_client.upload_file("data/arquivoteste.csv",
                    "m.rodrigo18-bucket-igti",
                     "data/arquivoteste.csv")
