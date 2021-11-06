# KeplerGl Earthquake Heatmap

This repo contains the heatmap of the 12892 earthquakes that took place in Turkey between 1910-2017, those on the richter scale of 3.0-7.2.

It enables the earthquake risk map published by official institutions to be compared with the actual earthquake data.

The earthquake data published by the [Kandilli Observatory](http://www.koeri.boun.edu.tr/new/en) were taken from [Kaggle](https://www.kaggle.com/caganseval/earthquake).

## Installing KeplerGl and Jupyter
Create a virtual environment
```
python -m venv venv
```
```
venv\Scripts\activate
```

Install packages
```
pip install keplergl
```
```
pip install jupyterlab
```
or
```
pip install -r requirements.txt
```

## Usage
```
jupyter lab
```
```
run keplergl.ipynb
```

![Turkey Earthquake Heatmap](https://github.com/gokhan-sari/examples/blob/main/images/turkey-earthquake-heatmap.jpg?raw=true "Turkey Earthquake Heatmap")
![Turkey Earthquake Risk Map](https://github.com/gokhan-sari/examples/blob/main/images/turkey-earthquake-risk-map.jpg?raw=true "Turkey Earthquake Risk Map")
