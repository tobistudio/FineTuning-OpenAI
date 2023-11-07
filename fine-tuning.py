import pandas as pd
import openai
import subprocess
import os

os.environ['OPENAI_API_KEY'] = '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'

# df = pd.read_csv("out_openai_completion.csv")

# prepared_data = df.loc[:,['sub_prompt','response_txt']]
# prepared_data.rename(columns={'sub_prompt':'prompt', 'response_txt':'completion'}, inplace=True)
# prepared_data.to_csv('prepared_data.csv',index=False)

# ## prepared_data.csv --> prepared_data_prepared.json
# subprocess.run('openai tools fine_tunes.prepare_data --file prepared_data.csv --quiet'.split())
# ## Start fine-tuning
# subprocess.run('openai api fine_tunes.create --training_file prepared_data_prepared.jsonl --model davinci --suffix "Rubi"'.split())

subprocess.run('openai api fine_tunes.follow -i ft-cvuugfMCZCV3nSQiTX4y0zuN'.split())
# subprocess.run('openai api fine_tunes.list'.split())


# List all created fine-tunes
# openai api fine_tunes.list