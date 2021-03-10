import pandas as pd

df = pd.read_csv(filepath_or_buffer='./frequence.txt',sep='\\s', names=['zi','freq','weight'])

zi = df[(df.zi >= '一') & ( df.zi <= '\u9fff') ]

zi.to_csv('zi.csv', index=False)