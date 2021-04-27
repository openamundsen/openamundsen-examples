import matplotlib.pyplot as plt
import pandas as pd

depth_obs = pd.read_csv('obs_snow_depth.csv', parse_dates=True, index_col=0, squeeze=True)
df_sim = pd.read_csv('results/point_proviantdepot.csv', parse_dates=True, index_col=0)
depth = pd.DataFrame(data=dict(obs=depth_obs, sim=df_sim.snow_depth))

plt.close('all')
depth.plot()
plt.ylabel('Snow depth (m)')
plt.show()
