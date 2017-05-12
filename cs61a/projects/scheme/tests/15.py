test = {
  'name': 'Problem 15',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x 1)
          c55ea5b1bca40acd76b8c213f8a08f8b
          # locked
          scm> (let ((x 5))
          ....    (+ x 3))
          29cbea0405f55882914cb294257af1c1
          # locked
          scm> x
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((a 1) (b a)) b)
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: SchemeError
          # choice: 1
          # choice: x
          # choice: y
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (let ((x 5))
          ....    (let ((x 2)
          ....          (y x))
          ....        (+ y (* x 2))))
          9cc890fba2180e73142276346c5369b9
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
    }
  ]
}
