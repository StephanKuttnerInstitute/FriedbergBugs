#!/usr/local/bin/python3
import pandas as pd

def main():
    df = pd.read_csv('./bug-reports.csv')
    f = open('./errors.md', 'w')
    f.write(df[['Citation','Column','Error','Correction']].to_markdown(index=False))
    f.close()

if __name__ == '__main__':
    main()
