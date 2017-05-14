test = {
  'name': 'Problem 13',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          True
          scm> (and 1 False)
          False
          scm> (and (+ 1 1) 1)
          1
          scm> (and False 5)
          False
          scm> (and 4 5 (+ 3 3))
          6
          scm> (and True False 42 (/ 1 0))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and True True True True))
          scm> (no-mutation)
          True
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and True True True True))
          """,
          'hidden': False,
          'locked': False
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
          scm> (or)
          False
          scm> (or (+ 1 1))
          2
          scm> (or False)
          False
          scm> (define (t) True)
          t
          scm> (or (t) 3)
          True
          scm> (or 5 2 1)
          5
          scm> (or False (- 1 1) 1)
          0
          scm> (or 4 True (/ 1 0))
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or False False False False))
          scm> (no-mutation)
          False
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or False False False False))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (greater-than-5 x) (if (> x 5) #t #f))
          greater-than-5
          scm> (define (other y) (or (greater-than-5 y) #f))
          other
          scm> (other 2)
          False
          scm> (other 6) ; test for mutation
          True
          scm> (define (other y) (and (greater-than-5 y) #t))
          other
          scm> (other 2)
          False
          scm> (other 6) ; test for mutation
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
