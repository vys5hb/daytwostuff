# %%
# This is my path
# /workspaces/daytwostuff
# %%
# This is my path after running a virtual environment
# /workspaces/daytwostuff
# The virtual environment is activated, but the terminal display path is the same
# %%
# I should include my environment in my repo so that it can be activated and replicated.
# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df.head()
# %%
# Extension Management:
# 2. The extension menus gives VS Code users access to a lot of features that help with quality of life
# and make coding easier
# 3. 
# - Data Wrangler gives a neat way to look at your data
# - Data Wrangler allows you to look at all types of data files, numpy arrays, data frames, etc.
# - Data Wrangler allows you to look at your data more in-depth, analyzing distribution of values, nulls values, means, medians, quartiles, etc.


# %%
# Package Managing:
# 5. We use a requirements.txt file so that we can easily replicate our environment, and a new user looking at your 
# code can easily install all the exact same packages and versions that you used when you created the project