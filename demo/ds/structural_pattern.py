
d = { 'name' : 'Proudct1', 'rate' : 20000}

match d:
    case {'price' : price}:
        print(price)
    case {'rate' : price}:
        print(price)

