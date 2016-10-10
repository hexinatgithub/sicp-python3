test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          07fa61723879693a70211246239795ee
          # locked
          >>> xk(10, 6)
          07fa61723879693a70211246239795ee
          # locked
          >>> xk(4, 6)
          3dcab9fe3b2b966fc0dea4bee36cfbe4
          # locked
          >>> xk(0, 0)
          dc549763a66595fb8475050be281005d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     elif x > 0:
          ...         print('small')
          ...     else:
          ...         print("nothin'")
          >>> how_big(7)
          fe4028bb37030ad778842d40ac93e700
          # locked
          >>> how_big(12)
          260c9a22fd4f3d2d25e08b6a0cd9d10e
          # locked
          >>> how_big(1)
          fdb47b226224360303fcfb56870d356a
          # locked
          >>> how_big(-1)
          760faed592aa321d30da37c71aa1c67b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def so_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     if x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('small')
          ...     print("nothin'")
          >>> so_big(7)
          fe4028bb37030ad778842d40ac93e700
          # locked
          >>> so_big(12)
          260c9a22fd4f3d2d25e08b6a0cd9d10e
          fe4028bb37030ad778842d40ac93e700
          # locked
          >>> so_big(1)
          fdb47b226224360303fcfb56870d356a
          760faed592aa321d30da37c71aa1c67b
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