from models.recipe import RecipeManager
from models.ingredient import IngredientManager

class GroceryListService:
  def __init__(self, recipe_manager, ingredient_manager):
    self.recipe_manager = recipe_manager
    self.ingredient_manager = ingredient_manager
