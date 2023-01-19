import pandas as pd
from scipy.stats import mannwhitneyu

df = pd.read_csv("resources/task2_data.csv")

nr_entities_relevant = df[df['relevanceJudge'] == 1]['#entities']
nr_entities_non_relevant = df[df['relevanceJudge'] == 0]['#entities']
nr_entities_relevant.describe()
nr_entities_non_relevant.describe()

u, p_value = mannwhitneyu(nr_entities_non_relevant, nr_entities_relevant)
print(u, p_value)
