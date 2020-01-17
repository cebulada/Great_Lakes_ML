## Great_Lakes_ML

## Authors

- [Daniel Adam Cebula](https://github.com/cebulada)
- [Rohan Chaudhari](https://github.com/focusrohan)

___

## Version 1.1.0

### Version 1.1.0 - Changes

Removed cloud functionality due to rising price concerns.

Local postgreSQL database, local flask server and local python server are now required to operate the API and Data Visualization website.

___

## Summary

After a long day of work you come home and you pour yourself a nice glass of water from your tap.  Before you drink you see an advisory stating that Lake Erie has higher than normal level of toxic algae and preventative measures need to be taken.

You are in Toronto so surely the water from the tap must be from Lake Ontario but how can you be sure.

The goal of this project was to see if machine learning algorithms can correctly classify the water source to one of the 4 great lakes by 25 parameters found in 2 datasets recovered from [Open Data Catalogue Ontario](https://data.ontario.ca/).

Please view [EXPLANATION.md](./EXPLANATION.md) for more in depth information as to how to set up local database, local flask server and local python server.

___

## Getting Started / Installation

Download the compressed [GitHub Repository](https://github.com/cebulada/Great_Lakes_ML.git)

OR

```
$ git clone https://github.com/cebulada/Great_Lakes_ML.git
```

THEN

Please read the instructions located in [EXPLANATION.md](./EXPLANATION.md).

These instruction will direct you to create a local postgreSQl database, local flask server and a local python server.

After performing these steps please observe [localhost:5000](https://localhost:5000/) for the API and [localhost:8000](https://localhost:5000/) for the data visualization.

___

## Prerequisites

### 1. Google Chrome, Mozilla Firefox and / or Internet Explorer 11 Web Browser Installed

### 2. Installation of Python 3.7.5 ([Instructions](https://www.python.org/downloads/release/python-375/))

### 3. Installation of Jupyter Notebook/Lab ([Instructions](https://jupyter.org/install))

### 4. Install Scientific Python Distribution ([Instructions](https://www.scipy.org/install.html))
#### Specifically pandas, NumPy and Matplotlib

### 5. Install the following dependencies in [requirements.txt](./requirements.txt). Use [pip](https://pypi.org/) or [conda](https://docs.conda.io/en/latest/)

___

## Versioning

[SemVer](http://semver.org/) for versioning.

___

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](./LICENSE.md) file for details

___