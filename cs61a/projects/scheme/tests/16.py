test = {
  'name': 'Problem 16',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define y 1)
          7f8ce7b9b26d2b5922718b99265fafdc
          # locked
          scm> (define f (mu (x) (+ x y)))
          17c5c9131eea78a6dfb3175a8e97e160
          # locked
          scm> (define g (lambda (x y) (f (+ x x))))
          280bf507069c60ae8be75781ba444342
          # locked
          scm> (g 3 7)
          824c8a87e1a23e1693a36ab2b26e2ceb
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
