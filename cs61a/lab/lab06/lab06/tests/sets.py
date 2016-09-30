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
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> sorted(a)  # Creates a sorted list
          71b467f9d598c71e1776228223d0336e
          # locked
          >>> a.add(4)
          >>> a.add(4)
          >>> a.remove(4)
          >>> 4 in a
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> a = {1, 4, 12, 1000}
          >>> sum(a)
          f954faedcaba9cf63717bd64f3a3c526
          # locked
          >>> b = {1, 2, 4}
          >>> sorted(a.intersection(b))
          384afd0b87c72e017ef37e90463fda92
          # locked
          >>> sorted(a & b)
          384afd0b87c72e017ef37e90463fda92
          # locked
          >>> sorted(a.union(b))
          f9e136f3df667430620540344543816c
          # locked
          >>> sorted(a | b)
          f9e136f3df667430620540344543816c
          # locked
          >>> sorted(a - b)
          db7dc8ae8306e1f8af390aebe96d5453
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> fruits = set(['apple', 'banana', 'tomato', 'apple'])
          >>> pizza = set(['cheese', 'tomato', 'flour'])
          >>> 'pepperoni' in pizza
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> fruits & pizza
          844d72211168903d6b1dbeb7621232e7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> t = [314, 15]
          >>> u = {89, 7, 15}
          >>> sorted(set(t) | u)
          04c5ae2622802f9227aeddbefb3a02c5
          # locked
          >>> u.add(6)
          >>> set(t) - u
          51991bcd3f4e29a20655b9820dbf993f
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
