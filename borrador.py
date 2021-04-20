import pandas

data = pandas.read_csv("prov_arg.csv")

provincias = data.to_dict()

provlist = data['Provincia'].to_list()

print(len(provlist))

    # print(prov['0'])
    # print(x['0'])
    # print(y['0'])