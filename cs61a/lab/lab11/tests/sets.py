test = {
  'name': 'Sets',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = [1, 1, 2, 2, 3, 3]
          >>> a = set(a)
          >>> len(a)
          3
          >>> sorted(a) # sorted(iterable) returns a new sorted list
          [1, 2, 3]
          >>> a.add(4)
          >>> a.add(4)
          >>> a.remove(4)
          >>> 4 in a
          False
          >>> a = {1, 4, 12, 1000}
          >>> sum(a)
          1017
          >>> b = {1, 2, 4}
          >>> sorted(a.intersection(b))
          [1, 4]
          >>> sorted(a & b)
          [1, 4]
          >>> sorted(a.union(b))
          [1, 2, 4, 12, 1000]
          >>> sorted(a | b)
          [1, 2, 4, 12, 1000]
          >>> sorted(a - b)
          [12, 1000]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> fruits = set(['apple', 'banana', 'tomato', 'apple'])
          >>> pizza = set(['cheese', 'tomato', 'flour'])
          >>> 'pepperoni' in pizza
          False
          >>> fruits & pizza
          {'tomato'}
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> t = [314, 15]
          >>> u = {89, 7, 15}
          >>> sorted(set(t) | u)
          [7, 15, 89, 314]
          >>> u.add(6)
          >>> set(t) - u
          {314}
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
