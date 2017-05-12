test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> global_frame = create_global_frame()
          >>> global_frame.define("x", 3)
          >>> global_frame.parent is None
          a48ad7c6cb9d8be0928e7032acab2fdd
          # locked
          >>> global_frame.lookup("x")
          ed2605996ac3b24d98b27c6d58145f06
          # locked
          >>> global_frame.define("x", 2)
          >>> global_frame.lookup("x")
          4b7283d4dfa392633549336acb032de7
          # locked
          >>> global_frame.lookup("foo")
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: None
          # choice: SchemeError
          # choice: 3
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> second_frame.parent == first_frame
          a48ad7c6cb9d8be0928e7032acab2fdd
          # locked
          >>> second_frame.lookup("x")
          ed2605996ac3b24d98b27c6d58145f06
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
