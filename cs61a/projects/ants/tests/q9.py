test = {
  'name': 'Problem 9',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing Remove
          >>> p0 = colony.places['tunnel_0_0']
          >>> p1 = colony.places['tunnel_0_1']
          >>> p0.add_insect(queen)
          >>> p1.add_insect(imposter)
          >>> p0.remove_insect(queen)
          >>> p1.remove_insect(imposter)
          >>> queen == p0.ant # Queen can't be removed
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> p1.ant      # Imposter should have been removed
          >>> queen.action(colony)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing queen place
          >>> colony_queen = ants.Place('Original Queen Location of the Colony')
          >>> ant_queen = ants.Place('Place given to the QueenAnt')
          >>> queen_place = ants.QueenPlace(colony_queen, ant_queen)
          >>> colony_queen.bees = [ants.Bee(1, colony_queen) for _ in range(3)]
          >>> ant_queen.bees = [ants.Bee(2, colony_queen) for _ in range(4)]
          >>> len(queen_place.bees)
          7cd035adf49fc93a635b4e8bb2e28bd4
          # locked
          >>> bee_armor = sum(bee.armor for bee in queen_place.bees)
          >>> bee_armor
          cda504d90147ee5bc48005ab0b5bf152
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing double damage
          >>> back = ants.ThrowerAnt()
          >>> thrower_damage = back.damage
          >>> front = ants.FireAnt()
          >>> fire_damage = front.damage
          >>> side_back = ants.ThrowerAnt()
          >>> side_front = ants.ThrowerAnt()
          >>> armor, side_armor = 20, 10
          >>> bee, side_bee = ants.Bee(armor), ants.Bee(side_armor)
          
          >>> colony.places['tunnel_0_0'].add_insect(back)
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> colony.places['tunnel_1_1'].add_insect(side_back)
          >>> colony.places['tunnel_1_3'].add_insect(side_front)
          >>> colony.places['tunnel_1_4'].add_insect(side_bee)
          
          >>> # Queen's attributes are correct
          >>> queen.damage
          1
          
          >>> # Simulate a battle in Tunnel 0 (contains Queen)
          >>> back.action(colony)  # No doubling until queen's action
          >>> bee.armor # if failed, damage doubled too early
          19
          >>> queen.action(colony)  # Queen should always deal normal damage
          >>> bee.armor # if failed, Queen damage incorrect
          18
          >>> bee.action(colony)  # Bee moves forward
          >>> colony.places['tunnel_0_3'].add_insect(front)  # Fire ant added
          >>> back.action(colony)  # Damage doubled in back
          >>> bee.armor  # if failed, back damage incorrect
          16
          >>> queen.action(colony)  # Queen should always deal normal damage
          >>> bee.armor # If failed, Queen damage incorrect (2)
          15
          >>> back.action(colony)  # Thrower damage still doubled
          >>> bee.armor # Back damage incorrect
          13
          >>> bee.action(colony)  # Fire damage doubled
          >>> bee.armor # if failed, Fire damage incorrect
          7
          
          >>> # Simulate a battle in Tunnel 1 (no Queen)
          >>> side_bee.armor  # if failed, side bee took damage when it shouldn't have
          10
          >>> side_back.action(colony)  # Ant in another tunnel: normal damage
          >>> side_bee.armor # If failed, side back damage is incorrect
          9
          >>> side_front.action(colony) # Ant in another tunnel: normal damage
          >>> side_bee.armor # If failed, side front damage is incorrect
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing Game ends when Queen place is infiltrated
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_1'].add_insect(queen)
          >>> colony.places['tunnel_0_2'].add_insect(bee)
          >>> queen.action(colony)
          >>> len(colony.queen.bees) <= 0 # If failed, Game ended before it should have
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> bee.action(colony)
          >>> len(colony.queen.bees) > 0 # Game should have ended
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing Imposter Queen
          >>> ant = ants.ThrowerAnt()
          >>> bee = ants.Bee(10)
          
          >>> colony.places['tunnel_0_0'].add_insect(queen)
          >>> colony.places['tunnel_0_1'].add_insect(imposter)
          >>> colony.places['tunnel_0_3'].add_insect(ant)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          
          >>> imposter.action(colony)
          >>> bee.armor   # Imposter should not damage bee
          d5486b8375bc63d70b73f741cd83d712
          # locked
          >>> ant.damage  # Imposter should not double damage
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          
          >>> queen.action(colony)
          >>> bee.armor   # Queen should damage bee
          8b5f7651e8464d241749041812e40bfa
          # locked
          >>> ant.damage  # Queen should double damage
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> ant.action(colony)
          >>> bee.armor   # If failed, ThrowerAnt has incorrect damage
          7cd035adf49fc93a635b4e8bb2e28bd4
          # locked
          
          >>> queen.armor   # Long live the Queen
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> imposter.armor  # Short-lived imposter
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing bodyguard doubling
          >>> bee = ants.Bee(3)
          >>> guard = ants.BodyguardAnt()
          >>> guard.damage = 5
          >>> colony.places['tunnel_0_1'].add_insect(queen)
          >>> colony.places['tunnel_0_1'].add_insect(guard)
          >>> colony.places['tunnel_0_2'].add_insect(bee)
          >>> queen.action(colony)
          >>> guard.damage # Bodyguard should be buffed
          10
          
          >>> queen.action(colony)
          >>> bee.armor   # QueenAnt should not have been buffed
          1
          >>> guard.damage  # Bodyguard should not be buffed twice
          10
          >>> len(colony.queen.bees) <= 0 # Game should not have ended
          True
          >>> bee.action(colony)
          >>> len(colony.queen.bees) > 0 # Game should have ended
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard contain doubling
          >>> guard = ants.BodyguardAnt()
          >>> guard.damage = 5
          >>> ant = ants.ThrowerAnt()
          >>> ant_doubled = 2 * ant.damage
          >>> colony.places['tunnel_0_1'].add_insect(queen)
          >>> colony.places['tunnel_0_3'].add_insect(guard)
          >>> colony.places['tunnel_0_3'].add_insect(ant)
          >>> queen.action(colony)
          >>> guard.damage # Bodyguard damage should have doubled
          10
          >>> ant.damage   # Contained ant should be buffed
          2
          
          >>> queen.action(colony)
          >>> guard.damage # Bodyguard should not be buffed twice
          10
          >>> ant.damage   # contained ant should not be buffed twice
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing that game still ends the old-fashioned way
          >>> bee = ants.Bee(3)
          >>> # The bee has an uninterrupted path to the heart of the colony
          >>> colony.places['tunnel_0_1'].add_insect(bee)
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> bee.action(colony)
          >>> len(colony.queen.bees) <= 0 # Game should not be over
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> queen.action(colony)
          >>> bee.action(colony)
          >>> len(colony.queen.bees) > 0 # Game should have ended
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing if queen will buff newly added ants
          >>> colony.places['tunnel_0_0'].add_insect(ants.ThrowerAnt())
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> # Add ant and buff
          >>> ant = ants.ThrowerAnt()
          >>> colony.places['tunnel_0_1'].add_insect(ant)
          >>> queen.action(colony)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> ant.action(colony)
          >>> bee.armor # Queen should buff new ants
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing if queen will not crash with no one to buff
          >>> colony.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(colony)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> colony.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(colony)
          >>> bee.armor # Queen should still hit the bee
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, imp
      >>> def queen_layout(queen, register_place, steps=5):
      ...     "Create a two-tunnel layout with water in the middle of 5 steps."
      ...     for tunnel in range(2):
      ...         exit = queen
      ...         for step in range(steps):
      ...             place = ants.Water if step == steps//2 else ants.Place
      ...             exit = place('tunnel_{0}_{1}'.format(tunnel, step), exit)
      ...             register_place(exit, step == steps-1)
      
      >>> imp.reload(ants)
      >>> hive = ants.Hive(ants.make_test_assault_plan())
      >>> colony = ants.AntColony(None, hive, ants.ant_types(), queen_layout)
      >>> queen = ants.QueenAnt()
      >>> imposter = ants.QueenAnt()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}