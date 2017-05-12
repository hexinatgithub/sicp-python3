test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a . b)")
          3532ae5b32471b54ce15eb21b6c34648
          # locked
          # choice: Pair('a', Pair('b'))
          # choice: Pair('a', Pair('b', nil))
          # choice: SyntaxError
          # choice: Pair('a', 'b')
          # choice: Pair('a', 'b', nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c)")
          e692789c7c63f2bde7f919c1b465402f
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('a', Pair('b', Pair('c')))
          # choice: Pair('a', 'b', 'c')
          # choice: Pair('a', Pair('b', 'c'))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c d)")
          0ed979b4743c825ef83e50de51d8a7c2
          # locked
          # choice: Pair('a', Pair('b', Pair('c', 'd')))
          # choice: Pair('a', Pair('b', 'c'))
          # choice: Pair('a', Pair('b', Pair('c', Pair('d', nil))))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . (b . (c . ())))")
          dc2bc33df30e1641789f3a91813ce8d5
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: SyntaxError
          # choice: Pair('a', Pair('b', Pair('c', Pair(nil, nil))))
          # choice: Pair('a', 'b', 'c')
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . ((b . (c))))")
          c64baf87d1740a159c24444a653f30f0
          # locked
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
          # choice: Pair('a', Pair('b', Pair('c', nil)), nil)
          # choice: Pair('a', Pair('b', Pair('c')), nil)
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil), nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(1 . 2)"]))
          >>> scheme_read(src)
          Pair(1, 2)
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
