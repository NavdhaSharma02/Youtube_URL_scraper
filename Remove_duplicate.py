# Removing duplicates based on the "URL" column aftet the Youtube_api code.

import pandas as pd
df = pd.read_csv('youtube_links.csv') 
df_cleaned = df.drop_duplicates(subset='URL')
df_cleaned.to_csv('cleaned_file.csv', index=False)
