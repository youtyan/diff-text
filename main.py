import os

import pandas as pd
import shutil

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if os.path.exists('data/output/a'):
        shutil.rmtree('data/output/a')
    if os.path.exists('data/output/b'):
        shutil.rmtree('data/output/b')
    os.mkdir('data/output/a')
    os.mkdir('data/output/b')

    df = pd.read_csv('data/input.csv', header=0, index_col=0)

    for index, row in df.iterrows():
        f = open(f'data/output/a/{index}.txt', 'w')
        f.write(row['TEXT1'])
        f.close()

        f = open(f'data/output/b/{index}.txt', 'w')
        f.write(row['TEXT2'])
        f.close()
