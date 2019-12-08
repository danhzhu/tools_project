# Squirrel Tracker Django Project
This is a Django based project that keeps track of all the known squirrels in Central Park. 
Users can easily add, update, and delete squirrel data, view squirrels on map, and know general stats about the squirrels.<br />
[Link to Server](https://psyched-throne-255421.appspot.com)<br />
[Linke to Clone](https://github.com/danhzhu/tools_project.git)

## Data Usage
[2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

## Main Features
### Management commands
- *Import* <br />
A command that imports the data from the 2018 census file to Sqlite3 database.
  ```
  $ python manage.py import_squirrel_data /path/to/file.csv
  ```
- *Export* <br />
A command that exports the data in database into csv file.
  ```
  $ python manage.py export_squirrel_data /path/to/file.csv
  ```
### Views
- *Map* <br />
  - A view that shows a map that displays the location of the squirrel sightings on an [OpenStreets](https://www.openstreetmap.org/about/) map.
  - Located at: ```/map```
  - Note that the browser will start to freeze if plotting more than 100 points at once,<br />
  so we randomly mark 50 at onece.
- *Squirrel ID List* <br />
  - A view that lists all squirrel sightings with links to edit and add sightings.
  - Located at: ```/sightings```
- *Squirrel Details* <br />
  - A view to update a particular sighting by the unique squirrel id
  - Once the submit button is clicked, the details of the squirrel will be updated.<br />
  Changes are able to view immediately.
  - Located at: ```/sightings/<unique-squirrel-id>```
- *Add New Squirrels* <br />
  - Users are able to create a new squirrel, and it will be added to the database automatically.<br />
  It will return to the list page if the new squirrel is successfully added.
  - Located at: ```/sightings/add```
- *General Stats* <br />
  - A view to display the general stats about all the squirrels.
  - Located at: ```/sightings/stats```

### Tools Used
- Django 2.2.7
- Python 3.7
- Google Cloud Platform

### Group Name: Group 20
### UNIs: [dz2423, sl4638]
