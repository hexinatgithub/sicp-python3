test = {
  'name': 'Problem 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, Pair(2, Pair(3, nil))))
          >>> global_frame.lookup('a')
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: 1
          # choice: 2
          # choice: 3
          # choice: SchemeError
          >>> frame.lookup('a')
          1d6ef7880cd9b59b64a1f4e1a1e35a12
          # locked
          >>> frame.lookup('b')
          4b7283d4dfa392633549336acb032de7
          # locked
          >>> frame.lookup('c')
          ed2605996ac3b24d98b27c6d58145f06
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(nil, nil)
          >>> frame.parent is global_frame
          a48ad7c6cb9d8be0928e7032acab2fdd
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
