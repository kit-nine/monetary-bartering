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
    weight = 40.08
class Strontium(Alkaline_Earth_Metal):
    weight = 87.62
class Barium(Alkaline_Earth_Metal):
    weight = 137.33
class Radium(Alkaline_Earth_Metal):
    weight = 226.02541

class Scandium(Transition_Metal):
    weight = 44.95591
class Titanium(Transition_Metal):
    weight = 47.867
class Vanadium(Transition_Metal):
    weight = 50.9415
class Chromium(Transition_Metal):
    weight = 51.996
class Manganese(Transition_Metal):
    weight = 54.93319
class Iron(Transition_Metal):
    weight = 55.84
class Cobalt(Transition_Metal):
    weight = 58.93319
class Nickel(Transition_Metal):
    weight = 58.693
class Copper(Transition_Metal):
    weight = 63.55
class Zinc(Transition_Metal):
    weight = 65.4
class Yttrium(Transition_Metal):
    weight = 88.90584
class Zirconium(Transition_Metal):
    weight = 91.22
class Niobium(Transition_Metal):
    weight = 92.90637
class Molybdenum(Transition_Metal):
    weight = 95.95
class Technetium(Transition_Metal):
    weight = 96.90636
class Ruthenium(Transition_Metal):
    weight = 101.1
class Rhodium(Transition_Metal):
    weight = 102.9055
class Palladium(Transition_Metal):
    weight = 106.42
class Silver(Transition_Metal):
    weight = 107.868
class Cadmium(Transition_Metal):
    weight = 112.41
class Hafnium(Transition_Metal):
    weight = 178.49
class Tantalum(Transition_Metal):
    weight = 180.9479
class Tungsten(Transition_Metal):
    weight = 183.84
class Rhenium(Transition_Metal):
    weight = 186.207
class Osmium(Transition_Metal):
    weight = 190.2
class Iridium(Transition_Metal):
    weight = 192.22
class Platinum(Transition_Metal):
    weight = 195.08
class Gold(Transition_Metal):
    weight = 196.96657
class Mercury(Transition_Metal):
    weight = 200.59
class Rutherfordium(Transition_Metal):
    weight = 267.122
class Dubnium(Transition_Metal):
    weight = 268.126
class Seaborgium(Transition_Metal):
    weight = 269.129
class Bohrium(Transition_Metal):
    weight = 270.133
class Hassium(Transition_Metal):
    weight = 269.1336
class Meitnerium(Transition_Metal):
    weight = 277.154
class Darmstadtium(Transition_Metal):
    weight = 282.166
class Roentgenium(Transition_Metal):
    weight = 282.169
class Copernicium(Transition_Metal):
    weight = 286.179

class Aluminum(Post_Transition_Metal):
    weight = 26.981538
class Gallium(Post_Transition_Metal):
    weight = 69.723
class Indium(Post_Transition_Metal):
    weight = 114.818
class Tin(Post_Transition_Metal):
    weight = 118.71
class Thallium(Post_Transition_Metal):
    weight = 204.383
class Lead(Post_Transition_Metal):
    weight = 207
class Bismuth(Post_Transition_Metal):
    weight = 208.98040
class Nihonium(Post_Transition_Metal):
    weight = 286.182
class Flerovium(Post_Transition_Metal):
    weight = 290.192
class Moscovium(Post_Transition_Metal):
    weight = 290.196
class Livermorium(Post_Transition_Metal):
    weight = 293.205

class Boron(Metalloid):
    weight = 10.81
class Silicon(Metalloid):
    weight = 28.085
class Germanium(Metalloid):
    weight = 72.63
class Arsenic(Metalloid):
    weight = 74.92159
class Antimony(Metalloid):
    weight = 121.760
class Tellurium(Metalloid):
    weight = 127.6
class Polonium(Metalloid):
    weight = 208.98243

class Fluorine(Halogen):
    weight = 18.99840316
class Chlorine(Halogen):
    weight = 35.45
class Bromine(Halogen):
    weight = 79.90
class Iodine(Halogen):
    weight = 126.9045
class Astatine(Halogen):
    weight = 209.98715
class Tennessine(Halogen):
    weight = 294.211

class Helium(Noble_Gas):
    weight = 4.00260
class Neon(Noble_Gas):
    weight = 20.180
class Argon(Noble_Gas):
    weight = 39.9
class Krypton(Noble_Gas):
    weight = 83.80
class Xenon(Noble_Gas):
    weight = 131.29
class Radon(Noble_Gas):
    weight = 222.01758
class Oganesson(Noble_Gas):
    weight = 295.216

class Lanthanum(Lanthanide):
    weight = 138.9055
class Cerium(Lanthanide):
    weight = 140.116
class Praseodymium(Lanthanide):
    weight = 140.90766
class Neodymium(Lanthanide):
    weight = 144.24
class Promethium(Lanthanide):
    weight = 144.91276
class Samarium(Lanthanide):
    weight = 150.4
class Europium(Lanthanide):
    weight = 151.964
class Gadolinium(Lanthanide):
    weight = 157.2
class Terbium(Lanthanide):
    weight = 158.29585
class Dysprosium(Lanthanide):
    weight = 162.500
class Holmium(Lanthanide):
    weight = 164.93033
class Erbium(Lanthanide):
    weight = 167.26
class Thulium(Lanthanide):
    weight = 168.93422
class Ytterbium(Lanthanide):
    weight = 173.05
class Lutetium(Lanthanide):
    weight = 174.9668

class Actinum(Actinide):
    weight = 
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