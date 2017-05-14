test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a . b)")
          Pair('a', 'b')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(a b . c)")
          Pair('a', Pair('b', 'c'))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(a b . c d)")
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(a . (b . (c . ())))")
          Pair('a', Pair('b', Pair('c', nil)))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(a . ((b . (c))))")
          Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
          """,
          'hidden': False,
          'locked': False
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
