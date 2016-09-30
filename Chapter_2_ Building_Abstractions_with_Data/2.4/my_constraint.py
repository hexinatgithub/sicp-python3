def connector(name=None):
    "A connector between constraints"
    informant = None
    constraints = []
    def set_val(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, ' = ', connector['val'])
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print("Connect Contraction: ", val, 'vs', value)
    def forget(source):
        nonlocal informant
        if source is informant:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten .')
            inform_all_except(source, 'forget', constraints)
    connector = {
        'set_val' : set_val,
        'forget'  : forget,
        'val'     : None,
        'has_val' : lambda: connector['val'] is not None,
        'connect' : lambda source: constraints.append(source)
    }
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints the message, except the source"""
    for c in constraints:
        if c is not source:
            c[message]()

from operator import add, sub
def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)

from operator import mul, truediv
def multiplier(a, b, c):
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraints that ab(a, b)=c, ca(c, a)=b, cb(c, b)=a"""
    def new_val():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif cv and av:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif cv and bv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {
        'new_val'    : new_val,
        'forget_val' : forget_value
    }
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def constant(connector, value):
    constant = {}
    connector['set_val'](constant, value)
    return constant

# ------------------------------------------------------------------------------

celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(x, 5)
    constant(w, 9)
    constant(y, 32)

converter(celsius, fahrenheit)

celsius['set_val']('user', 25)