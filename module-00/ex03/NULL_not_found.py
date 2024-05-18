def NULL_not_found(object: any) -> int:
  try:
    # check is value falsy and for NaN
    if (bool(object) == True and object == object):
      raise ValueError(object)
    
    type_of_obj: type = type(object)
    title = type_of_obj.__name__.title()

    if (object is None):
      title = "Nothing"
    elif (type_of_obj is int):
      title = "Zero"
    elif (type_of_obj is float):
      title = "Cheese"
    elif (type_of_obj is str):
      title = "Empty"
    elif (type_of_obj is bool):
      title = "Fake"

    print(f"{title} : {object} {type_of_obj}")
    return 0
  except Exception as e:
    print("Type not Found")
    return 1