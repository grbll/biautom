from importlib.resources import files

test = files("resources")
print(test.joinpath("json").name)
