from .upgrader_weak import Weak
# from .upgrader_moderate import Moderate
# from .upgrader_strong import Strong

class Upgrader:
  def __init__(self):
    pass

  def weak(self, validator):
    weak_upgrader = Weak(validator)
    weak_upgrader.weak_info()

  def moderate(self, validator):
    print("Moderate upgrade not implemented yet.")

  def strong(self, validator):
    print("Strong upgrade not implemented yet.")