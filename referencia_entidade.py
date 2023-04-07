import os

def extract_name(name):
    return name.split(".")[0]

def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for colunm in read_lines(filename):
        if colunm:
            values = colunm.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            metadata.append((nome, tipo, desc))
    return metadata

def main() -> object:
    meta = {}

    keys = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    print("entidade {} -> {}".format(key, col[0]))

if __name__ == "__main__":
    main()