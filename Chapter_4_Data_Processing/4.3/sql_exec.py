"""An interpreter for a limited subset of SQL select statements.

Complete statements
-------------------
create_table: create table [name] as [select_statement]
select_statement: select [expressions] <from [tables]>
                                       <where [expression]>
                                       <order by [expression]>
                  OR
                  [select_statement] union [select_statement]

Sub-statements
--------------
tables (comma-separated): [name] <as [name]>
expressions (comma-separated): [expression] <as [name]>
expression: Python-syntax expression

Above, [] is a placeholder for a required part and <> is an optional part.
"""

import itertools
import re

from collections import namedtuple

built_in_eval = eval
def eval(expr, env):
    return built_in_eval(expr, env)

##########
# Parser #
##########

keywords = ["create table", "select", "from", "where", "union", "order by"]
keyword_pattern = re.compile(r"(\b{}\b)".format(r"\b|\b".join(keywords)), re.I)
name_pattern = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
comment_prefix = "--"

def tokenize(lines):
    """Split lines into keywords and stuff in between, dropping comments."""
    no_comments = []
    for line in lines.split("\n"):
        if comment_prefix in line:
            line = line[:line.index(comment_prefix)]
        no_comments.append(line)
    tokens = re.split(keyword_pattern, " ".join(no_comments))
    for token in tokens:
        t = token.strip(" \t;")
        if t:
            yield t.replace("=", "==").replace("<>", "!=").replace("||", "+").replace("!==", "!=")

def parse(tokens, select_only=False):
    """Parse the next statement or expression in tokens, a Buffer."""
    if pop_if(tokens, "create table") and not select_only:
        name_as = tokens.pop().strip()
        assert name_as.endswith(" as"),  "'as' required: " + str(tokens)
        return CreateTable(name_as[:-3], parse(tokens, True))
    elif pop_if(tokens, "select"):
        assert tokens.current(), "columns expected: " + str(tokens)
        columns = tokens.pop()
        tables, where, order_by = None, None, None
        if pop_if(tokens, "from"):
            check_tables(tokens.current(), tokens)
            tables = tokens.pop()
        if pop_if(tokens, "where"):
            assert tokens.current(), "where condition expected: " + str(tokens)
            where = tokens.pop()
        if pop_if(tokens, "order by"):
            assert tokens.current(), "order condition expected: " + str(tokens)
            order_by = tokens.pop()
        select = Select(columns, tables, where, order_by)
        if pop_if(tokens, "union"):
            return Union(select, parse(tokens, True))
        else:
            return select
    elif select_only:
        assert False, "select expected: " + + str(tokens)
    else:
        assert False, "select or create table expected: " + str(tokens)

def check_tables(tables, tokens):
    """Assert that tables description is well-formed."""
    for elem in [t.strip() for t in tables.split(",")]:
        ok = " " not in elem or (elem.count(" ") == 2 and " as " in elem)
        assert ok, "Bad table description " + str(tokens)

def pop_if(tokens, token):
    """If tokens.current() == token, pop it and return True."""
    if tokens.current() == token:
        tokens.pop()
        return True
    else:
        return False

#############
# Evaluator #
#############

class CreateTable:
    def __init__(self, name, select):
        self.name = name
        self.select = select

    def __repr__(self):
        return "create table {} as {}".format(self.name, self.select)

    def execute(self, env):
        """Create a table and bind it to name in env, then return no rows."""
        env[self.name] = list(self.select.execute(env))
        return ()

class Union:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} union {}".format(self.left, self.right)

    def execute(self, env):
        """Yield rows from left and then right, always using left's type."""
        lefts = list(self.left.execute(env))
        for left in lefts:
            left_type = type(left)
            yield left
        for right in self.right.execute(env):
            yield left_type(*right)

class Select:
    """select [columns] from [tables] where [condition] order by [order]."""
    def __init__(self, columns, tables, condition, order):
        self.columns = columns
        self.tables = tables
        self.condition = condition
        self.order = order
        self.make_row = create_make_row(self.columns)

    def execute(self, env):
        """Join, filter, sort, and map rows from tables to columns."""
        from_rows = join(self.tables, env)
        filtered_rows = filter(self.filter, from_rows)
        ordered_rows = self.sort(filtered_rows)
        return map(self.make_row, ordered_rows)

    def filter(self, row):
        env = dict(row)
        if self.condition:
            return eval(self.condition, env)
        else:
            return True

    def sort(self, rows):
        if self.order:
            return sorted(rows, key=lambda r: eval(self.order, r))
        else:
            return rows

    def __repr__(self):
        s = "select " + self.columns
        if self.tables:
            s += " from " + self.tables
        if self.condition:
            s += " where " + self.condition
        if self.order:
            s += " order by " + self.order
        return s

def create_make_row(description):
    """Return a function from an input env (dict) to an output row (tuple).

    description -- a comma-separated list of [expression] <as [column name]>
    """
    columns = [c.strip() for c in description.split(",")]
    expressions = []
    names = ["column_" + str(i) for i in range(len(columns))] # Default names
    for i, column in enumerate(columns):
        if " as " in column:
            column, names[i] = split_on_as(column)
        elif name_pattern.fullmatch(column):
            names[i] = column
        expressions.append(column)
    if expressions == ["*"]:
        return lambda env: env["*"]
    else:
        row = namedtuple("Row", names)
        return lambda env: row(*[eval(e, env) for e in expressions])

def join(tables, env):
    """Return an iterator over dictionaries from names to values in a row.

    tables -- a comma-separate sequences of [global name] as [local name]
    env    -- a dictionary from global names to tables
    """
    if not tables:
        return [{}]
    names, aliases = zip(*[name_and_alias(t) for t in tables.split(",")])
    joined_rows = itertools.product(*[env[name] for name in names])
    return map(lambda rows: make_env(rows, aliases), joined_rows)

def make_env(rows, aliases):
    """Create an environment of unambiguous names in rows and aliases."""
    env = dict(zip(aliases, rows))
    env["*"] = sum(rows, ())
    for row in rows:
        for name in row._fields:
            if name not in env:
                env[name] = getattr(row, name)
            elif name in env and name not in aliases:
                del env[name] # ambiguous name is removed from env
    return env

#############
# Utilities #
#############

class Buffer:
    """A buffer of tokens."""
    def __init__(self, tokens):
        self.popped = []
        self.tokens = list(tokens)

    def pop(self):
        if self.tokens:
            token = self.tokens.pop(0)
            self.popped.append(token)
            return token
        else:
            return None

    def current(self):
        if self.tokens:
            return self.tokens[0]
        else:
            return None

    def __str__(self):
        return ' '.join(self.popped) + ' >> ' + ' '.join(self.tokens)

def name_and_alias(description):
    """Return (name, alias) pair for [name] <as [alias]>."""
    if " as " in description:
        return split_on_as(description)
    else:
        return [description.strip()] * 2

def split_on_as(description):
    """Split on "as" and verify that the second element is a simple name."""
    parts = [s.strip() for s in description.split(" as ")]
    assert len(parts) == 2, "Malformed as expression: " + description
    assert name_pattern.fullmatch(parts[1]), "Bad name: " + parts[1]
    return parts

global_env = {}

def execute(lines):
    tokens = Buffer(tokenize(lines))
    statement = parse(tokens)
    result = statement.execute(global_env)
    return result

