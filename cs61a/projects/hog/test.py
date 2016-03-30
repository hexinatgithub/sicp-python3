import hog
hog.four_sided = hog.make_test_dice(1)
hog.six_sided = hog.make_test_dice(3)
always = hog.always_roll
s0, s1 = hog.play(always(5), always(3), score0=36, score1=15, goal=50)
print(s0, s1)