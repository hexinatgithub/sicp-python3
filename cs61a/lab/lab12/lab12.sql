.read fa16data.sql
.read sp17data.sql

CREATE TABLE obedience AS
  select seven, hilfinger from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 16 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number FROM students AS a, fa16students AS b
    WHERE a.date = b.date AND a.color = b.color AND a.pet = b.pet;

CREATE TABLE sevens AS
  SELECT s.seven FROM students AS s, checkboxes AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b 
    WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;
