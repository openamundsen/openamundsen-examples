import openamundsen as oa

config = oa.read_config('proviantdepot.yml')
model = oa.OpenAmundsen(config)
model.initialize()
model.run()
