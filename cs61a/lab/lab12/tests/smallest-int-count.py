test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 40;
          1|30
          2|7
          3|5
          4|7
          5|3
          6|5
          7|13
          8|3
          9|6
          10|3
          11|4
          12|5
          13|14
          14|8
          15|2
          16|3
          17|7
          18|2
          19|7
          20|1
          21|2
          22|3
          23|10
          24|3
          25|2
          26|3
          27|2
          28|3
          29|5
          31|2
          32|2
          33|1
          34|6
          36|2
          37|6
          39|1
          41|2
          42|2
          43|1
          46|3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
