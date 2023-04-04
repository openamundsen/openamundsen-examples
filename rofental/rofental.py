import openamundsen as oa

config = oa.read_config('rofental.yml')
model = oa.OpenAmundsen(config)
model.initialize()
model.run()
