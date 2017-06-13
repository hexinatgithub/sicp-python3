create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select DISTINCT name, size from dogs, sizes where min < height and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from parents, dogs where parent == name order by height desc;

-- Sentences about siblings that are the same size
create table sentences as
  with siblings(sibling1, sibling2) as (
    select A.child, B.child 
            from parents A, parents B
                  where A.parent == B.parent and A.child < B.child
  )
  select A.sibling1 || " and " || A.sibling2 || " are " || B.size || " siblings"
          from siblings A, size_of_dogs B, size_of_dogs C
                where A.sibling1 == B.name and A.sibling2 == C.name and B.size == C.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with temp(name_path, numbers, last_height, total_height) as (
    select name, 1, height, height from dogs union
    select a.name_path || ", " || b.name, a.numbers + 1, b.height, a.total_height + b.height
            from temp a, dogs b where a.last_height < b.height and a.numbers < 4
  )
  select name_path, total_height from temp where total_height >= 170 order by total_height;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    with ints(n) as (
      select 1 union
      select n + 1 from ints where n < 100
    ),
    temp(n, numbers) as (
      select a.n, count(*) from ints a, ints b where a.n >= b.n and (a.n % b.n) == 0
                                  group by a.n
    )
    select n, numbers from temp order by n;

create table primes as
    select n from divisors where numbers == 2
