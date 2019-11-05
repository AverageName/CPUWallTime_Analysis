import os
import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import argparse
import yaml


def parse_yaml(yaml_path):
    stream = open(yaml_path, "r")
    data = yaml.safe_load(stream)
    return data


def read_csv(root_dir, csv_file):
    data = pd.read_csv(os.path.join(root_dir, csv_file), delimiter=';')
    return data


def filter_data(data, params):
    for key in params.keys():
        if type(params[key][0]) == int:
            data = data.loc[(data[key] >= params[key][0]) & (data[key] <= params[key][1])]
        elif type(params[key][0]) == str:
            data = data.loc[(data[key].isin(params[key]))]
    return data


def get_value_by_key(data, key):
    return np.array(data[key].to_list())


def save_plot_get_values(data, name, path, x_scale):
    plt.figure()
    ax = sns.distplot(data / x_scale, hist=False, kde=True, axlabel=name)
    ax.set_yticklabels([])

    filename = name + '.png'
    plt.savefig(filename)
    os.replace(os.path.join('.', filename), os.path.join(path, filename))

    xs = ax.get_lines()[0].get_data()[0]
    ys = ax.get_lines()[0].get_data()[1]
    return [xs, ys]


def save_values(xs, ys, name):
    filename = name + '_points.csv'
    csv_file = open(os.path.join('.', filename), 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, dialect='excel')
    wr.writerow(('#', 'x', 'y'))
    for i in range(len(xs)):
        wr.writerow((i + 1, '{0:.10f}'.format(xs[i]), '{0:.10f}'.format(ys[i])))


#  Parser for script.
parser = argparse.ArgumentParser(description="Script for CPUWallTime Graphs")
parser.add_argument("--yaml_path", dest="yaml_path", type=str, help="path to yaml config file")

args = parser.parse_args()

params = parse_yaml(args.yaml_path)
data = read_csv(params["root_dir"], params["csv_file"])
data = filter_data(data, params["filters"])

# TODO: add output to csv file.
# TODO: Add which graph to plot in configs

plot_name = params["plot_name"]
xs_ys = save_plot_get_values(get_value_by_key(data, plot_name), plot_name, params["dest_path"], params["x_scale"])
save_values(xs_ys[0], xs_ys[1], plot_name)
