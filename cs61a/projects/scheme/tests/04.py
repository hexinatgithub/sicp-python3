test = {
  'name': 'Problem 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> plus = PrimitiveProcedure(scheme_add) # + procedure
          >>> scheme_apply(plus, twos, env)
          5dc34dbe25d53109ac62b4184b75a40f
          # locked
          # choice: 4
          # choice: SchemeError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> twos = Pair(2, Pair(2, nil))
          >>> oddp = PrimitiveProcedure(scheme_oddp) # odd? procedure
          >>> scheme_apply(oddp, twos, env)
          0b51df1e150843e094f5a67945b0c704
          # locked
          # choice: True
          # choice: False
          # choice: SchemeError
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
