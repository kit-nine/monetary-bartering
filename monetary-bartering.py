# the monetary bartering system consists of basic imaginary currency, units. every item is given a set unit value. the values of all items in one's possession combined is their value, and there are no units outside real items. the base for 1 unit is a single hi-chew (50 grams), and items are valued on their weight. the value of the unit does not change, but resource farming can technically cause inflation.
#there will be an item class, a person class, and a trade function, which includes a reference to a person's trading methods.

# The class system for every known thing made of matter so the system can generate the items
# Based on "List of states of matter" (https://en.wikipedia.org/wiki/List_of_states_of_matter) page on Wikipedia, and all links on that page.
class Item:
    pass

class Solid(Item):
    value_multiplier = 
class Amorphous_solid(Solid):
    definition = "Solid which does not exhibit crystalline structure."
    value_multiplier = 
class Nano_structured_materials(Amorphous_solid):
    pass
class Amorphous_thin_films(Amorphous_solid):
    pass
class Soils(Amorphous_solid):
    pass
class Crystalline_solid(Solid):
    pass
class Plastic_crystal(Solid):
    pass
class Quasi_crystal(Solid):
    pass

class Liquid(Item):
    pass
class Liquid_crystal(Liquid):
    pass

class Gas(Item):
    pass

class Plasma(Item):
    pass

class Supercritical_fluid(Item):
    pass

class Degenerate_matter(Item):
    pass
class Electron_degenerate_matter(Degenerate_matter):
    pass
class Neutron_degenerate_matter(Degenerate_matter):
    pass
class Strange_matter(Degenerate_matter):
    pass
class Quantum_spin_Hall_state(Degenerate_matter):
    pass

class Bose_Einstin_condensate(Item):
    pass

class Fermionic_condensate(Item):
    pass

class Superconducitivity(Item):
    pass

class Superfluid(Item):
    pass

class Supersolid(Item):
    pass

class Quantum_spin_liquid(Item):
    pass

class String_net_liquid(Item):
    pass

class Time_crystals(Item):
    pass

class Rydberg_polaron(Item):
    pass

class Black_superionic_ice(Item):
    pass

class Quark_gluon_plasma(Item):
    pass
