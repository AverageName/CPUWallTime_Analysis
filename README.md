# CPU Wall Time analysis script

Easy script for plotting and saving propability density function of CPU Wall time to concrete folder.

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
  &nbsp;&nbsp;&nbsp;&nbsp;2.7 **tables_path**: Path where to save csv files with plots <br/>
  3. Open your terminal or command line and write <br/>  &nbsp;&nbsp;&nbsp;&nbsp; ```python script.py --yaml_path your_path_to_yaml``` <br/> &nbsp;&nbsp;&nbsp;&nbsp; where your_path_to_yaml is path to your yaml-config file.<br/>
