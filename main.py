material = []
inventory = []

def init_inventory_by_material():
  f = open("cooking_ro.csv","r")
  for i in range(1,242,2):
    f.readline()
    line = f.readline().split(",")
    for j in range(1,6):
      if(line[j]=="-" or line[j]=='-' or line[j] ==" "):
        continue
      elif(line[j] not in material):
        material.append(line[j])
  f.close()
  material.sort()

def create_inventory_file():
  f = open("inventory.csv","w")
  for word in material:
    f.write(word+", 0\n")
  f.close()

def init():
  init_inventory_by_material()
  create_inventory_file()

#-----------------------------------------------------------

def find_cookable_food():
  f = open("inventory.csv","r")
  for i in range(1,43):
    line = f.readline().split(",")
    line[1] = int(line[1])
    if(line[1]>0):
      inventory.append(line[0])
  f.close()

  f = open("cooking_ro.csv","r")
  for i in range(1,242,2):
    f.readline()
    line = f.readline().split(",")
    err = 0
    for j in range(1,6):
      if(line[j] == "–"):
        continue
      if(line[j] not in inventory):
        err=1
        break
    if(err==1):
      continue
    else:
      print(line)

def main():
  find_cookable_food()

if __name__ == '__main__':
    main()
