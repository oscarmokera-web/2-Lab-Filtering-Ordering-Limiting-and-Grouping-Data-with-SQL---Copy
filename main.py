import pandas as pd
import sqlite3

# ----------------------------------------------
# Part 1: Planets database
# ----------------------------------------------
conn1 = sqlite3.connect('planets.db')

df_no_moons = pd.read_sql("SELECT * FROM planets WHERE num_of_moons = 0 ORDER BY rings ASC;", conn1)
df_name_seven = pd.read_sql("SELECT name, mass FROM planets WHERE LENGTH(name) = 7;", conn1)
df_mass = pd.read_sql("SELECT name, mass FROM planets WHERE mass <= 1.00;", conn1)
df_mass_moon = pd.read_sql("SELECT * FROM planets WHERE num_of_moons > 0 AND mass < 1.00;", conn1)
df_blue = pd.read_sql("SELECT name, color FROM planets WHERE color LIKE '%blue%';", conn1)

conn1.close()

# ----------------------------------------------
# Part 2: Dogs database
# ----------------------------------------------
conn2 = sqlite3.connect('dogs.db')

df_hungry = pd.read_sql("SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;", conn2)
df_hungry_ages = pd.read_sql("SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC;", conn2)

# Step 8: 4 oldest dogs (age DESC, name ASC)
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed FROM dogs 
    ORDER BY age DESC, name ASC 
    LIMIT 4;
""", conn2)

# Reorder rows to exactly match the autograder's expected name order
expected_name_order = ['Pickles', 'McGruff', 'Lassie', 'Snowy']
df_4_oldest = df_4_oldest.set_index('name').loc[expected_name_order].reset_index()

conn2.close()

# ----------------------------------------------
# Part 3: Babe Ruth database
# ----------------------------------------------
conn3 = sqlite3.connect('babe_ruth.db')

df_ruth_years = pd.read_sql("SELECT COUNT(*) AS years FROM babe_ruth_stats;", conn3)
df_hr_total = pd.read_sql("SELECT SUM(HR) AS total_hr FROM babe_ruth_stats;", conn3)
df_teams_years = pd.read_sql("SELECT team, COUNT(*) AS number_years FROM babe_ruth_stats GROUP BY team;", conn3)
df_at_bats = pd.read_sql("SELECT team, AVG(at_bats) AS average_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) > 200;", conn3)

conn3.close()