import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
This counts only arxiv papers, meaning a few papers from this list aren't in the graph
"""


readme = open("README.md").read()

data_string = re.findall("\*.*arxiv.org\/abs\/(\d{2})(\d{2})", readme)
data = np.array([2000 + int(year) + int(month) / 12 for year, month in data_string])

plt.rcParams["figure.figsize"] = (8,4.8)
plt.hist(data, 168, cumulative="True")
plt.xticks(range(2010, 2024, 2))
plt.title("CT ∩ ML: Cumulative number of papers through time")
plt.xlabel("Year")
plt.ylabel("Total number of papers")
plt.show()
