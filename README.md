# CPU Wall Time analysis script

Easy script for plotting and saving probability density function of CPU Wall time to concrete folder.

## Requirements
  ### Environment: 
  Python 3.7, pip.
  ### Packages: 
  * pandas 0.25.1
  * numpy 1.16.5
  * scipy 1.3.1
  * matplotlib 3.1.1
  * argparse 
  * PyYAML 5.1.2
  * sklearn 0.0
  ### Intalling packages:
  1. For CentOS and Ubuntu:<br/>
  &nbsp;&nbsp;&nbsp;&nbsp; 1.1 run ```chmod +x install_with_pip.sh ```.<br/>
  &nbsp;&nbsp;&nbsp;&nbsp; 1.2 run ```./install_with_pip.sh``` to install packages from the terminal.<br/>
  2. For Windows install packages from your IDE terminal with: ```pip install package_name==version_number```.
  

## Documentation
  ### How to run script:<br/>
  1. Git clone the repo.<br/>
  2. Configure your parameters in yaml config file:<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.1 **root-dir**: Root directory for your csv-file with data.<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.2 **csv-file**: Name of your csv file<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.3 **filters**: (you can input any of parameters from csv file) <br/>
  &nbsp;&nbsp;&nbsp;&nbsp; For example:<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.1 WallDurationSeconds: [1000, 10000] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.2 NumberCPU: [2, 25] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.3 Nodes: [1, 10] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3.4 QueueName: ["long", "short"] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.4 **dest_path**: Destination path where to save your graph <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.5 **x_scale**: Scale for x-axis <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.6 **plot_name**: Name of parameter you want to plot <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.7 **plot_type**: Type of plot <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.7.1 "hist" - histogram (only for string values of parameter you want to plot)<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.7.2 "df" - density function (only for numeric values of parameter you want to plot)<br/>
  &nbsp;&nbsp;&nbsp;&nbsp;2.8 **tables_path**: Path where to save csv files with plots <br/>
  &nbsp;&nbsp;To add new parameter you need to write string like this in config file: <br/>
  &nbsp;&nbsp;&nbsp;parameter_name: [min, max] (for int type) <br/>
  &nbsp;&nbsp;&nbsp;parameter_name: ["long", "short", "infi"] (for str type)
  3. Open your terminal or command line and write <br/>  &nbsp;&nbsp;&nbsp;&nbsp; ```python script.py --yaml_path your_path_to_yaml``` <br/> &nbsp;&nbsp;&nbsp;&nbsp; where your_path_to_yaml is path to your yaml-config file.<br/>
