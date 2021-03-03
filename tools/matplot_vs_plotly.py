#%%
import matplotlib.pyplot as plt

year = [1500, 1600, 1700, 1800, 1900, 2000]
pop = [458, 580, 682, 1000, 1650, 6127]

if True:
    plt.plot(year, pop)
    plt.show()
#%%

#%%
import plotly.express as px

year = [1500, 1600, 1700, 1800, 1900, 2000]
pop = [458, 580, 682, 1000, 1650, 6127]

fig = px.line(x=year, y=pop)
fig.show()
#%%