# Proviantdepot

openAMUNDSEN point-scale setup for station Proviantdepot (2737 m a.s.l., Rofental, Ötztal Alps,
Austria) in the winter season 2019/20.

Sources for the meteorological and snow measurements in this data set:
https://doi.pangaea.de/10.1594/PANGAEA.919324 and https://doi.pangaea.de/10.1594/PANGAEA.928595.

To run this example, either execute the `proviantdepot.py` script from within the current directory
or run `openamundsen proviantdepot.yml` from the command line.
Model results are stored in CSV format in the `results` directory.
The `plot_results.py` script produces a plot of observed against the resulting simulated snow depth
(requires matplotlib to be installed).
