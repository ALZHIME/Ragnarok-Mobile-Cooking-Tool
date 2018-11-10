# Ragnarok-Mobile-Cooking-Tool
  Find menu that you can cook in game base on your inventory
  
## main.py
  there are init() and find_cookable_food() <br />
  - ### init()
    - init is use to remodelling inventory file depend on cooking_ro.csv
  - ### find_cookable_food()
    - find cookable food depend on your inventory

## cooking_ro.csv pattern is
  NAME_IN_ENGLISH <br />
  NAME, MATERIAL_1, MATERIAL_2, MATERIAL_3, MATERIAL_4, MATERIAL_5 <br />
  > if it require 4 or less material others material will be -
  
## inventory.csv pattern is
  NAME_OF_MAETERIAL, AMOUNT
