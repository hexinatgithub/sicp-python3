test = {
  'name': 'primes',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from primes;
          2
          3
          5
          7
          11
          13
          17
          19
          23
          29
          31
          37
          41
          43
          47
          53
          59
          61
          67
          71
          73
          79
          83
          89
          97
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw09.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
