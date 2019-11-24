import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import yaml
import time
import sys
from sklearn.neighbors import KernelDensity


def parse_yaml(yaml_path):
    stream = open(yaml_path, "r")
    data = yaml.safe_load(stream)
    return data


def read_csv(root_dir, csv_file):
    data = pd.read_csv(os.path.join(root_dir, csv_file), delimiter=';')
    return data


def filter_data(data, params):
    if params is not None:
        for key in params.keys():
            if type(params[key][0]) in [int, float]:
                data = data.loc[(data[key] >= params[key][0]) & (data[key] <= params[key][1])]
            elif type(params[key][0]) == str:
                data = data.loc[(data[key].isin(params[key]))]
            print(key, params[key][0], params[key][1])
    return data


def get_value_by_key(data, key):
    return np.array(data[key].to_list())


def save_png(name, path):
    filename = name + '.png'
    plt.savefig(filename)
    os.replace(os.path.join('.', filename), os.path.join(path, filename))


def save_plot_get_values(data, name, path, x_scale):
    fig, ax = plt.subplots()
    if data.shape[0] == 0:
        print("No data with this parameters, try another configuration")
        sys.exit(0)
    if params["plot_type"] == "hist":
        if type(data[0]) != np.str_:
            print("Can't plot hist")
            sys.exit(0)
        counts, bins, bars = plt.hist(data)
        plt.title(name)
        save_png(name, path)
        plt.show()
        ys = []
        for i in counts:
            if i > 0:
                ys.append(i)
        return [np.unique(data), ys]
    elif params["plot_type"] == "df":
        if type(data[0]) not in [np.int32, np.float32]:
            print("Can't plot df")
            sys.exit(0)
        data = data / x_scale
        if data.shape[0] == 1:
            model = KernelDensity(bandwidth=1, kernel="gaussian")
        else:
            model = KernelDensity(bandwidth=1.06 * np.std(data) * (data.shape[0] ** (-1/5)) + 1e-6, kernel="gaussian")
        model.fit(data.reshape(-1, 1))
        values = np.linspace(np.min(data) - 2, np.max(data) + 2, 100)
        values = values.reshape(-1, 1)
        probs = np.exp(model.score_samples(values))
        ax.plot(values, probs)
        ax.set_yticklabels([])
        plt.title(name)
        save_png(name, path)
        plt.show()

        xs = ax.get_lines()[0].get_data()[0]
        ys = ax.get_lines()[0].get_data()[1]
        return [xs, ys]
    else:
        print("Wrong plot type")
        sys.exit(0)


def save_values(xs, ys, name, table_path):
    filename = name + '_points.csv'
    csv_file = open(os.path.join(table_path, filename), 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, dialect='excel', lineterminator='\n')
    wr.writerow(('#', 'x', 'y'))
    if type(xs[0]) == np.str_:
        for i in range(len(xs)):
            wr.writerow((i + 1, xs[i], ys[i]))
    else:
        for i in range(len(xs)):
            wr.writerow((i + 1, '{0:.10f}'.format(xs[i]), '{0:.10f}'.format(ys[i])))


#  Parser for script.
start = time.time()
parser = argparse.ArgumentParser(description="Script for CPUWallTime Graphs")
parser.add_argument("--yaml_path", dest="yaml_path", type=str, help="path to yaml config file")

args = parser.parse_args()

params = parse_yaml(args.yaml_path)
data = read_csv(params["root_dir"], params["csv_file"])
data = filter_data(data, params["filters"])
plot_name = params["plot_name"]

xs_ys = save_plot_get_values(get_value_by_key(data, plot_name), plot_name, params["dest_path"], params["x_scale"])

if params["plot_type"] != "str":
    save_values(xs_ys[0], xs_ys[1], plot_name, params["tables_path"])
# print("Time: ", time.time() - start)

# python script.py --yaml_path config.yml
