from pathlib import Path

import numpy as np
import openamundsen as oa

config = oa.read_config('rofental.yml')

# Calculate openness-based snow redistribution factor field based on the
# parameters by Hanzer et al. (2016)
srf_file = oa.util.raster_filename('srf', config)
if not srf_file.exists():
    print('Calculating openness...')
    dem_file = oa.util.raster_filename('dem', config)
    meta = oa.fileio.read_raster_metadata(dem_file, crs=config.crs)
    dem = oa.fileio.read_raster_file(dem_file)
    no5000 = oa.terrain.openness(dem, config.resolution, 5000, negative=True)
    no50 = oa.terrain.openness(dem, config.resolution, 100, negative=True)
    srf = ((3 * (no5000 - 1)).clip(min=0.1, max=1.6) + (3 * (no50 - 1.2)).clip(min=0.1, max=1.6)) / 2.
    print(f'Writing snow redistribution file to {srf_file}')
    oa.fileio.write_raster_file(srf_file, srf, meta['transform'])

model = oa.OpenAmundsen(config)
model.initialize()
shape = model.grid.shape

# Initialize ice layer
ice_thickness = oa.fileio.read_raster_file(oa.util.raster_filename('ice_thickness', config))
icies = ice_thickness > 0
ice_density = np.full(shape, np.nan)
ice_density[icies] = model.config.snow.cryolayers.transition.ice
ice_we = np.zeros(shape)
ice_we[icies] = ice_thickness[icies] * ice_density[icies]
model.state.snow.ice_content[-1, :, :] = ice_we
model.state.snow.density[-1, :, :] = ice_density
model.state.snow.thickness[-1, :, :] = ice_thickness

# Initialize firn layer
firn_we = oa.fileio.read_raster_file(oa.util.raster_filename('firn_we', config))
firnies = firn_we > 0
firn_density = np.full(shape, np.nan)
firn_density[firnies] = 600.
firn_thickness = np.zeros(shape)
firn_thickness[firnies] = firn_we[firnies] / firn_density[firnies]
model.state.snow.ice_content[-2, :, :] = firn_we
model.state.snow.density[-2, :, :] = firn_density
model.state.snow.thickness[-2, :, :] = firn_thickness

model.run()
