import raisingexceptions

flock = raisingexceptions.Flock()
donald = raisingexceptions.Duck()
daisy = raisingexceptions.Duck()
duck3 = raisingexceptions.Duck()
duck4 = raisingexceptions.Duck()
duck5 = raisingexceptions.Duck()
duck6 = raisingexceptions.Duck()
duck7 = raisingexceptions.Duck()
percy = raisingexceptions.Penguin()
# percy = raisingexceptions.Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()
