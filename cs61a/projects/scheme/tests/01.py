test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 ", "(+ 23 4)) ("]))
          >>> src.current()
          c88ae7c644d2c96ad650a00028bff2c4
          # locked
          >>> src.remove_front()
          c88ae7c644d2c96ad650a00028bff2c4
          # locked
          >>> src.current()
          d71d84fd6e177113edf056534e6e8313
          # locked
          >>> src.remove_front()
          d71d84fd6e177113edf056534e6e8313
          # locked
          >>> src.remove_front()
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          >>> scheme_read(src)
          6c4217f08dee3ab8c574e916e1c826a8
          # locked
          >>> src.current()
          a2c805835d058917490ddf30d0951443
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(+ 23 4)'])))
          6c4217f08dee3ab8c574e916e1c826a8
          # locked
          >>> read_line('(+ 23 4)')  # Shorter version of above!
          6c4217f08dee3ab8c574e916e1c826a8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          76b14f86e886c2669945a79c3bc272f4
          # locked
          >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
          cda024250e0f59f6fb50beedd5aa96a7
          # locked
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          b7862fa62d0476ab4f2798cb40bedf50
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          79220544ffe5bd238e524375b10bc4fc
          # locked
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
          # choice: Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': True
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
