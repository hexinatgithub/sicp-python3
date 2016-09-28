test = {
  'name': 'List Comprehension',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [x*x for x in range(5)]
          243aa8e2bd3dbb66adabedc08e6a72d0
          # locked
          >>> [n for n in range(10) if n % 2 == 0]
          e492984ef9eae20981375facbea325bb
          # locked
          >>> ones = [1 for i in ["hi", "bye", "you"]]
          >>> ones + [str(i) for i in [6, 3, 8, 4]]
          e461b7d532978a0843bce0ed9cf4d483
          # locked
          >>> [i+5 for i in [n for n in range(1,4)]]
          2e7da5c2d413ca4e8f43833b79758dc3
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
          >>> [i**2 for i in range(10) if i < 3]
          9b2ea6ec16fc5ffe329d1ad60302b7c3
          # locked
          >>> lst = ['hi' for i in [1, 2, 3]]
          >>> print(lst)
          4585a7c516df027541d727773e5c1b7c
          # locked
          >>> lst + [i for i in ['1', '2', '3']]
          0826ebcaba067ffc666e42380fbbea1e
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
