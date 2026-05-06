import pandas as pd
import sqlite3

# ----------------------------------------------
# Part 1: Planets database
# ----------------------------------------------
conn1 = sqlite3.connect('planets.db')

# Step 1: planets with 0 moons (column is 'num_of_moons')
df_no_moons = pd.read_sql("SELECT * FROM planets WHERE num_of_moons = 0 ORDER BY rings ASC;", conn1)

# Step 2: planets with name length exactly 7 letters (name and mass)
df_name_seven = pd.read_sql("SELECT name, mass FROM planets WHERE LENGTH(name) = 7;", conn1)

# Step 3: planets with mass <= 1.00 (name and mass)
df_mass = pd.read_sql("SELECT name, mass FROM planets WHERE mass <= 1.00;", conn1)

# Step 4: planets with at least one moon and mass < 1.00 (all columns)
df_mass_moon = pd.read_sql("SELECT * FROM planets WHERE num_of_moons > 0 AND mass < 1.00;", conn1)

# Step 5: planets with color containing 'blue' (name and color)
df_blue = pd.read_sql("SELECT name, color FROM planets WHERE color LIKE '%blue%';", conn1)

conn1.close()

# ----------------------------------------------
# Part 2: Dogs database
# ----------------------------------------------
conn2 = sqlite3.connect('dogs.db')

# Step 6: hungry dogs (hungry=1), sorted by age youngest to oldest
df_hungry = pd.read_sql("SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;", conn2)

# Step 7: hungry dogs age 2 to 7 inclusive, sorted alphabetically by name
df_hungry_ages = pd.read_sql("SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC;", conn2)

# Step 8: 4 oldest dogs, then result sorted alphabetically by breed
df_4_oldest = pd.read_sql("SELECT name, age, breed FROM (SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4) ORDER BY breed ASC;", conn2)

conn2.close()

# ----------------------------------------------
# Part 3: Babe Ruth database
# ----------------------------------------------
conn3 = sqlite3.connect('babe_ruth.db')

# Step 9: total number of years played
df_ruth_years = pd.read_sql("SELECT COUNT(*) AS years FROM babe_ruth_stats;", conn3)

# Step 10: total career home runs (column 'HR')
df_hr_total = pd.read_sql("SELECT SUM(HR) AS total_hr FROM babe_ruth_stats;", conn3)

# Step 11: number of years per team
df_teams_years = pd.read_sql("SELECT team, COUNT(*) AS number_years FROM babe_ruth_stats GROUP BY team;", conn3)

# Step 12: teams averaging >200 at bats (column 'at_bats')
df_at_bats = pd.read_sql("SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200;", conn3)

conn3.close()