import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    '../data/rofental/validation/proviantdepot_valid.csv',
    index_col=0,
    parse_dates=True,
)
depth_obs = df['USH9 snow depth (mm)'] / 1000
df_sim = pd.read_csv('results/point_proviantdepot.csv', parse_dates=True, index_col=0)
depth = pd.DataFrame(
    data=dict(
        obs=(
            depth_obs
            .loc['2019-10-01 00:00':'2020-06-30 23:00']
            .resample(df_sim.snow_depth.index.inferred_freq)
            .mean()
        ),
        sim=df_sim.snow_depth,
    ),
)

plt.close('all')
depth.plot()
plt.ylabel('Snow depth (m)')
plt.show()
