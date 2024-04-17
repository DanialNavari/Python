import pysynth_b as psb # a, b, e, and s variants available

song = (('c', 6),('d', 6),('e', 6),('e', 6),
        ('e', 6),('e', 6),('e', 6),('g', 6),('e', 3),
        ('e', 6),('g', 6),('e', 6), ('g', 6),('e', 3),
        ('e', 6),('f', 6),('d', 6),('e', 6),('c', 3),
        ('d', 6),('e', 6),('d', 6),('e', 6),('c', 3),
        ('c', 6),('d', 6),('c', 6),('d', 6),('c', 3),
        ('g', 6),('f', 6),('e', 6),('f', 6),('e', 3))

# Beats per minute (bpm) is really quarters per minute here
psb.make_wav(song, fn = "song.wav", leg_stac = .7, bpm = 180)