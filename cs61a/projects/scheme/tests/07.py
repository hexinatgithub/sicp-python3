test = {
  'name': 'Problem 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '103495fc3358e1b6354d1d4a277039e6',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          506108214132d6cb9c307edb2f9d0f8b
          # locked
          scm> 'hello
          506108214132d6cb9c307edb2f9d0f8b
          # locked
          scm> ''hello
          11e53d0ebd5fcb87953db84e824e20c7
          # locked
          # choice: (quote hello)
          # choice: hello
          # choice: (hello)
          # choice: (quote (quote (hello)))
          scm> (quote (1 2))
          e0115c13325291c6a30393eff9777ee4
          # locked
          scm> '(1 2)
          e0115c13325291c6a30393eff9777ee4
          # locked
          scm> (quote (1 . 2))
          9a8a33947ee1cd41aa91f5f15184c47b
          # locked
          scm> '(1 . (2))
          e0115c13325291c6a30393eff9777ee4
          # locked
          scm> (car '(1 2 3))
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          scm> (cdr '(1 2))
          1c70ebb4f1aabfcbe22f96bda497dd0b
          # locked
          scm> (car (car '((1))))
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          scm> (quote 3)
          ed2605996ac3b24d98b27c6d58145f06
          # locked
          scm> (eval (cons 'car '('(4 2))))
          5dc34dbe25d53109ac62b4184b75a40f
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> read_line(" (quote x) ")
          55894b325c4c2817733a8a1223c79f1e
          # locked
          >>> read_line(" 'x ")
          55894b325c4c2817733a8a1223c79f1e
          # locked
          # choice: Pair('x', nil)
          # choice: 'x'
          # choice: Pair('quote', 'x')
          # choice: Pair('quote', Pair('x', nil))
          >>> read_line(" (a b) ")
          6e7962ce0515005f1aa1ece26c1f9f99
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '(a b) ")
          1af43453acd78705e072b903fe9ce759
          # locked
          # choice: Pair('a', Pair('b', nil))
          # choice: Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
          # choice: Pair('quote', Pair('a', 'b'))
          # choice: Pair('quote', Pair('a', Pair('b', nil)))
          >>> read_line(" '((a)) ")
          6b34a9dd52ff83f52d5e6953f2d7375f
          # locked
          # choice: Pair('quote', Pair(Pair('a', nil), nil))
          # choice: Pair('quote', Pair(Pair('a', nil), nil), nil)
          # choice: Pair('quote', Pair(Pair('a'), nil))
          # choice: Pair('quote', Pair(Pair('a'), nil), nil)
          # choice: Pair('quote', Pair(Pair(Pair('a', nil), nil), nil))
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
