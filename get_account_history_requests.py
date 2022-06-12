import argparse
import pandas as pd
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--requests',
                    type=str,
                    default='request.txt')
parser.add_argument('--output',
                    type=str,
                    default='account_history.csv')
args = parser.parse_args()

response1 = None
response2 = None

# execfile(args.requests)
print('requests file :', args.requests)
with open(args.requests) as file:
    exec(file.read())

if response1 is None:
    raise ValueError

if response2 is None:
    data = response1.text
else:
    dataA = response1.text.split('</table>')
    dataB = json.loads(response2.text)['html']
    data = dataA[0] + dataB + dataA[1]
tables = pd.read_html(data)
df = tables[0]
df = df.droplevel(level=0, axis=1)

print('transactions :', len(df.index))
print('output file :', args.output)
df.to_csv(args.output)
