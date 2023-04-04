import openamundsen as oa
from pathlib import Path

config = oa.read_config('rofental.yml')

# Calculate openness-based snow redistribution factor field based on the
# parameters by Hanzer et al. (2016)
srf_file = Path('./data/rofental/srf_rofental_50.asc')
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
model.run()
