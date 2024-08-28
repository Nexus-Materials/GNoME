from nequip import default_config
from gnome import model_from_config
cfg = default_config()
cfg.scale = 1.0
cfg.shift = 0.0
model = model_from_config(cfg)
print(model)  #sucessfully constructed the model