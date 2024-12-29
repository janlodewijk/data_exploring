import requests
import pandas as pd

url = 'https://api.data.amsterdam.nl/dcatd/datasets/yvlbMxqPKn1ULw/purls/1/subsidies_openbaar_subsidieregister.csv'
response = requests.get(url)
response.raise_for_status()

from io import StringIO
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data)

print(df.head())

