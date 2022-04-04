# %%
import drawdata as dd
# %%
dd.draw_scatter()
# %%
help(dd)
# %%
import pandas as pd
# %%
a = pd.read_clipboard(sep=",")
# %%
dd.draw_histogram()
# %%
b = pd.read_clipboard(sep=",")
# %%
dd.draw_line()
# %%
c = pd.read_clipboard(sep=",")
# %%
c
# %%
