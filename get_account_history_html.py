import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--html',
                    type=str,
                    default='account_history.html')
parser.add_argument('--output',
                    type=str,
                    default='account_history.csv')
args = parser.parse_args()

print('html file :', args.html)
tables = pd.read_html(args.html)
df = tables[0]
df = df.droplevel(level=0, axis=1)
df = df[df['Date'].notna()]

print('transactions :', len(df.index))
print('output file :', args.output)
df.to_csv(args.output)
