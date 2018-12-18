# Rental Data Analysis on ImmoScout
This project includes a collection of scripts/classes to get the data from ImmoScout, perform a statistical analysis on the rental data, and display the resulting analysis on an interactive Choropleth map. 

## ImmoScout Scraper

The class `ImmoScout` converts the `rental` data on ImmoScout and can save it as a `csv` file. 

**Example**:

```python
from ImmoScout import ImmoScout
import pandas as pd

# instantiate the ImmoScout class by setting the city name and listing type
lausanne = ImmoScout(city_name = 'lausanne', list_type = 'rent')

# if some data is already downloaded set 'in_path' to the already saved csv file,
# otherwise just set the output path, i.e., out_path to save the converted data
lausanne.to_csv(in_path = '', out_path='../data/lausanne.csv')

# convert the csv to pandas data frame
df = pd.read_csv('../data/lausanne.csv')
```

Here is the first 5 rows of `df`:

<div  style="overflow:auto;">
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Id</th>
      <th>SurfaceArea</th>
      <th>NumRooms</th>
      <th>Type</th>
      <th>Address</th>
      <th>Description</th>
      <th>Rent</th>
      <th>Bookmark</th>
      <th>Link</th>
      <th>RentPerArea</th>
      <th>RentPerRoom</th>
      <th>AreaPerRoom</th>
      <th>ZipCode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>4695812</td>
      <td>41.0</td>
      <td>2.0</td>
      <td>flat</td>
      <td>Av. de Cour 65, 1007 Lausanne, VD</td>
      <td>Appartement de 2 pièces au 5ème étage</td>
      <td>NaN</td>
      <td>New</td>
      <td>/en/d/flat-rent-lausanne/4695812?s=2&amp;t=1&amp;l=202...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20.500000</td>
      <td>1007</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5204125</td>
      <td>21.0</td>
      <td>1.5</td>
      <td>studio</td>
      <td>Route Aloys-Fauquez 122, 1018 Lausanne, VD</td>
      <td>Studio proche de toutes les commodités</td>
      <td>970.0</td>
      <td>New</td>
      <td>/en/d/studio-rent-lausanne/5204125?s=2&amp;t=1&amp;l=2...</td>
      <td>46.190476</td>
      <td>646.666667</td>
      <td>14.000000</td>
      <td>1018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>5201717</td>
      <td>95.0</td>
      <td>4.0</td>
      <td>flat</td>
      <td>Av. de Morges 39, 1004 Lausanne, VD</td>
      <td>Joli appartement - centre ville proche commodités</td>
      <td>2085.0</td>
      <td>NaN</td>
      <td>/en/d/flat-rent-lausanne/5201717?s=2&amp;t=1&amp;l=202...</td>
      <td>21.947368</td>
      <td>521.250000</td>
      <td>23.750000</td>
      <td>1004</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5201713</td>
      <td>29.0</td>
      <td>1.5</td>
      <td>flat</td>
      <td>Ch. du Devin 57, 1012 Lausanne, VD</td>
      <td>Quartier de Chailly, spacieux 1.5 pièce</td>
      <td>910.0</td>
      <td>NaN</td>
      <td>/en/d/flat-rent-lausanne/5201713?s=2&amp;t=1&amp;l=202...</td>
      <td>31.379310</td>
      <td>606.666667</td>
      <td>19.333333</td>
      <td>1012</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5195729</td>
      <td>11.0</td>
      <td>NaN</td>
      <td>single-room</td>
      <td>Chemin de Montolivet 19, 1006 Lausanne, VD</td>
      <td>1006 Lausanne - Montolivet 19 - Chambre meublé...</td>
      <td>560.0</td>
      <td>NaN</td>
      <td>/en/d/single-room-rent-lausanne/5195729?s=2&amp;t=...</td>
      <td>50.909091</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1006</td>
    </tr>
  </tbody>
</table>
</div>



## Rental data analysis

For the rental data analysis see [this](https://github.com/hamedrazavi/rental_analysis_switzerland_immoscout24/blob/master/src/rental_analysis_lausanne.ipynb) notebook. [Here](https://hamedrazavi.github.io/articles/rental_analysis.html) is a quick article which include the resulting maps. 

