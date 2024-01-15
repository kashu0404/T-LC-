# T-LC: Think and Look Clean
1.) Watch the demo on this link -->
2.) To replicate this project:
  Clone the repository
  Go to: https://dev.mysql.com/downloads/ to install MySQL and the MySQL Workbench
  First, Click MySQL Community Server to install MySQL that is compatible with your machine.
  Then, click MySQL Workbench and install one compatible with your machine
  Once everything is setup create a database called: "TlcProject"
  Make a table called: "materialsTable"
  Create a table with the following structure:
  
+------------------+-------------------------------+---------+
| idmaterialsTable | material                      | quality |
+------------------+-------------------------------+---------+
|                1 | cupro                         | low		 |
|                2 | cupra                         | low     |
|                3 | rayon                         | low     |
|                4 | polyester                     | low     |
|                5 | nylon                         | low     |
|                6 | cotton                        | low     |
|                7 | viscose                       | low     |
|                8 | elastane                      | low     |
|                9 | econyl                        | good    |
|               10 | recycled polyester            | good    |
|               11 | Modal                         | good    |
|               12 | Sheep Wool                    | good    |
|               13 | Merino Wool                   | good    |
|               14 | Cashmere                      | good    |
|               15 | Upcycled Leather              | good    |
|               16 | Down                          | good    |
|               17 | Silk                          | good    |
|               18 | recycled cotton               | good    |
|               19 | Vegetable Tanned Leather      | good    |
|               20 | hemp                          | high    |
|               21 | linen                         | high    |
|               22 | organic cotton                | high    |
|               23 | bamboo linen                  | high    |
|               24 | deadstock                     | high    |
|               25 | tencel                        | high    |
|               26 | Bamboo Lyocell                | high    |
|               27 | ecovero                       | high    |
|               28 | Piñatex                       | high    |
|               29 | Bananatex                     | high    |
|               30 | Scoby Leather                 | high    |
|               31 | S.Cafe                        | high    |
|               32 | Brewed Protein                | high    |
|               33 | Apple Leather                 | high    |
|               34 | Woocoa                        | high    |
|               35 | QMilk                         | high    |
|               36 | Alpaca wool                   | high    |
|               37 | Camel wool                    | high    |
|               38 | Yak Wool                      | high    |
|               39 | cork                          | high    |
|               40 | LivaEco Viscose               | high    |
|               41 | wool                          | high    |
|               42 | LENZING™ ECOVERO™ Viscose     | high    |
|               43 | polyamide                     | low     |
|               44 | spandex                       | low     |
+------------------+-------------------------------+---------+

Here is the description for the column information:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| idmaterialsTable | int         | NO   | PRI | NULL    |       |
| material         | varchar(45) | YES  |     | NULL    |       |
| quality          | varchar(45) | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
Example:
CREATE TABLE TlcProject.materialsTable (
    idmaterialsTable INT NOT NULL PRIMARY KEY,
    material VARCHAR(45) NULL,
    quality VARCHAR(45) NULL
);

INSERT INTO TlcProject.materialsTable (idmaterialsTable, material, quality)
VALUES (1, 'cupro', 'low');

Similarly insert the rest of the materials to the table.


NOTE: Whichever directory you create your project, create a file named: ".env" and fill in this information. This file is required for the searchResult.html to work.

  MYSQL_HOST='localhost'
  MYSQL_USER='sqluser'
  MYSQL_PASSWORD='mypassword'
  MYSQL_DATABASE='TlcProject'

  If you run into issues with the authentication protocol when connecting to the database check out this webpage:
  https://www.geeksforgeeks.org/how-to-connect-to-mysql-server-using-vs-code-and-fix-errors/




