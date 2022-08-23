# the monetary bartering system consists of basic imaginary currency, units. every item is given a set unit value. the values of all items in one's possession combined is their value, and there are no units outside real items. the base for 1 unit is 50 grams, and items are valued on their weight. the value of the unit does not change, but resource farming can technically cause inflation.
#there will be an item class, a person class, and a trade function, which includes a reference to a person's trading methods.

# The periodic table split into a class structure so the system can create every possible thing on earth and define its value based on its weight, 50 grams = 1 unit
# Chemical Groups:
class Nonmetal:
    pass
class Alkali_Metal:
    pass
class Alkaline_Earth_Metal:
    pass
class Transition_Metal:
    pass
class Post_Transition_Metal:
    pass
class Metalloid:
    pass
class Halogen:
    pass
class Noble_Gas:
    pass
class Lanthanide:
    pass
class Actinide:
    pass

class Hydrogen(Nonmetal):
    weight = 1.0080
class Carbon(Nonmetal):
    weight = 12.011
class Nitrogen(Nonmetal):
    weight = 14.007
class Oxgen(Nonmetal):
    weight = 15.999
class Phosphorus(Nonmetal):
    weight = 30.97376200
class Sulfur(Nonmetal):
    weight = 32.07
class Selenium(Nonmetal):
    weight = 78.97

class Lithium(Alkali_Metal):
    weight = 7.0
class Sodium(Alkali_Metal):
    weight = 22.9897693
class Potassium(Alkali_Metal):
    weight = 39.0983
class Rubidium(Alkali_Metal):
    weight = 85.468
class Cesium(Alkali_Metal):
    weight = 132.9054520
class Francium(Alkali_Metal):
    weight = 223.01973

class Beryllium(Alkaline_Earth_Metal):
    weight = 9.012183
class Magnesium(Alkaline_Earth_Metal):
    weight = 24.305
class Calcium(Alkaline_Earth_Metal):
    weight = 
class Strontium(Alkaline_Earth_Metal):
    pass
class Barium(Alkaline_Earth_Metal):
    pass
class Radium(Alkaline_Earth_Metal):
    pass

class Scandium(Transition_Metal):
    pass
class Titanium(Transition_Metal):
    pass
class Vanadium(Transition_Metal):
    pass
class Chromium(Transition_Metal):
    pass
class Manganese(Transition_Metal):
    pass
class Iron(Transition_Metal):
    pass
class Cobalt(Transition_Metal):
    pass
class Nickel(Transition_Metal):
    pass
class Copper(Transition_Metal):
    pass
class Zinc(Transition_Metal):
    pass
class Yttrium(Transition_Metal):
    pass
class Zirconium(Transition_Metal):
    pass
class Niobium(Transition_Metal):
    pass
class Molybdenum(Transition_Metal):
    pass
class Technetium(Transition_Metal):
    pass
class Ruthenium(Transition_Metal):
    pass
class Rhodium(Transition_Metal):
    pass
class Palladium(Transition_Metal):
    pass
class Silver(Transition_Metal):
    pass
class Cadmium(Transition_Metal):
    pass
class Hafnium(Transition_Metal):
    pass
class Tantalum(Transition_Metal):
    pass
class Tungsten(Transition_Metal):
    pass
class Rhenium(Transition_Metal):
    pass
class Osmium(Transition_Metal):
    pass
class Iridium(Transition_Metal):
    pass
class Platinum(Transition_Metal):
    pass
class Gold(Transition_Metal):
    pass
class Mercury(Transition_Metal):
    pass
class Rutherfordium(Transition_Metal):
    pass
class Dubnium(Transition_Metal):
    pass
class Seaborgium(Transition_Metal):
    pass
class Bohrium(Transition_Metal):
    pass
class Hassium(Transition_Metal):
    pass
class Meitnerium(Transition_Metal):
    pass
class Darmstadtium(Transition_Metal):
    pass
class Roentgenium(Transition_Metal):
    pass
class Copernicium(Transition_Metal):
    pass

class Aluminum(Post_Transition_Metal):
    pass
class Gallium(Post_Transition_Metal):
    pass
class Indium(Post_Transition_Metal):
    pass
class Tin(Post_Transition_Metal):
    pass
class Thallium(Post_Transition_Metal):
    pass
class Lead(Post_Transition_Metal):
    pass
class Bismuth(Post_Transition_Metal):
    pass
class Nihonium(Post_Transition_Metal):
    pass
class Flerovium(Post_Transition_Metal):
    pass
class Moscovium(Post_Transition_Metal):
    pass
class Livermorium(Post_Transition_Metal):
    pass

class Boron(Metalloid):
    pass
class Silicon(Metalloid):
    pass
class Germanium(Metalloid):
    pass
class Arsenic(Metalloid):
    pass
class Antimony(Metalloid):
    pass
class Tellurium(Metalloid):
    pass
class Polonium(Metalloid):
    pass

class Fluorine(Halogen):
    pass
class Chlorine(Halogen):
    pass
class Bromine(Halogen):
    pass
class Iodine(Halogen):
    pass
class Astatine(Halogen):
    pass
class Tennessine(Halogen):
    pass

class Helium(Noble_Gas):
    pass
class Neon(Noble_Gas):
    pass
class Argon(Noble_Gas):
    pass
class Krypton(Noble_Gas):
    pass
class Xenon(Noble_Gas):
    pass
class Radon(Noble_Gas):
    pass
class Oganesson(Noble_Gas):
    pass

class Lanthanum(Lanthanide):
    pass
class Cerium(Lanthanide):
    pass
class Praseodymium(Lanthanide):
    pass
class Neodymium(Lanthanide):
    pass
class Promethium(Lanthanide):
    pass
class Samarium(Lanthanide):
    pass
class Europium(Lanthanide):
    pass
class Gadolinium(Lanthanide):
    pass
class Terbium(Lanthanide):
    pass
class Dysprosium(Lanthanide):
    pass
class Holmium(Lanthanide):
    pass
class Erbium(Lanthanide):
    pass
class Thulium(Lanthanide):
    pass
class Ytterbium(Lanthanide):
    pass
class Lutetium(Lanthanide):
    pass

class Actinum(Actinide):
    pass
class Thorium(Actinide):
    pass
class Protactinium(Actinide):
    pass
class Uranium(Actinide):
    pass
class Neptunium(Actinide):
    pass
class Plutonium(Actinide):
    pass
class Americum(Actinide):
    pass
class Curium(Actinide):
    pass
class Berkelium(Actinide):
    pass
class Californium(Actinide):
    pass
class Einstienium(Actinide):
    pass