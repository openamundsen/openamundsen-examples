import openamundsen as oa

config = oa.read_config('proviantdepot_t-index.yml')
model = oa.OpenAmundsen(config)
model.initialize()
model.run()
