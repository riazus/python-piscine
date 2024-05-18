def all_thing_is_obj(object: any) -> int:
  type_of_obj: type = type(object)
  title = type_of_obj.__name__.title()

  if (type_of_obj is str):
    title = f"{object} is in the kitchen"
  elif (type_of_obj is int):
    print("Type not found")
    return 42
  
  print(f"{title} : {type_of_obj}")
  return 42