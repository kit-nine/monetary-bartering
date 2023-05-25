"""
a ʇ is a unit, and each item is valued in units based on its
ppm in the earth's crust, lower ppms becoming higher ʇs. the
conversion between ppm and ʇ is the reciprocal of ppm / 1000000.

to figure out something's value in units, first figure out
what percentage of the object is made up of what elements.
input the weight of the object, the elements that the object
consists of, and the percentages of each element in the object.

then divide the value by avogadro's number * 100000 and round it off to the hundredths place
"""

MILLION = 1000000

def ppm_to_units(ppm):
    return 1 / (ppm / MILLION)

def value_an_object(weight, elements_percentages):
    object_value = 0
    for i in elements_percentages:
        i_value = ppm_to_units(elements_ppms.get(i))
        j = elements_percentages.get(i)
        num_atoms = ((weight * j) / elements_amus.get(i)) * 602000000000000000000000.00123
        object_value += (i_value * num_atoms)
    return '%.2f'%(object_value / (60200000000000000000000000123))

elements_ppms = {"H" : 703.74, "C" : 206.29, "N" : 780849.5, "O" : 293584.67, "P" : 1050, "S" : 350, "SE" : 0.05, "LI" : 20, "NA" : 23600, "K" : 20900, "RB" : 90, "CS" : 3, "FR" : 0.000000000000000001, "BE" : 2.8, "MG" : 23300, "CA" : 41500, "SR" : 370, "BA" : 425, "RA" : 0.0000009, "SC" : 22, "TI" : 5650, "V" : 120, "CR" : 102, "MN" : 950, "FE" : 56300, "CO" : 25, "NI" : 84, "CU" : 60, "ZN" : 70, "Y" : 33, "ZR" : 165, "NB" : 20, "MO" : 1.2, "TC" : 0.000000000135, "RU" : 0.001, "RH" : 0.001, "PD" : 0.015, "AG" : 0.075, "CD" : 0.15, "HF" : 3.0, "TA" : 2.0, "W" : 1.25, "RE" : 0.0007, "OS" : 0.0015, "IR" : 0.001, "PT" : 0.005, "AU" : 0.004, "HG" : 0.085, "AL" : 82300, "GA" : 19, "IN" : 0.25, "SN" : 2.3, "TL" : 0.85, "PB" : 14, "BI" : 0.0085, "B" : 10, "SI" : 282000, "GE" : 1.5, "AS" : 1.8, "SB" : 0.2, "TE" : 0.001, "PO" : 0.0000000002, "F" : 585, "CL" : 145, "BR" : 2.4, "I" : 0.45, "AT" : 0.00000000000000000003, "HE" : 2.624, "NE" : 9.09255, "AR" : 4671.75, "KR" : 0.57005, "XE" : 0.00003, "RN" : 0.0000000000004, "LA" : 39, "CE" : 66.5, "PR" : 9.2, "ND" : 41.5, "PM" : 0.00000000000000002, "SM" : 7.05, "EU" : 2, "GD" : 6.2, "TB" : 1.2, "DY" : 5.2, "HO" : 1.3, "ER" : 3.5, "TM" : 0.52, "YB" : 3.2, "LU" : 0.8, "AC" : 0.0000000000006, "TH" : 9.6, "PA" : 0.000014, "U" : 2.7, "NP" : 0.000000000003, "PU" : 0.00000000003}

elements_amus = {'H' : 1.008,'HE' : 4.003, 'LI' : 6.941, 'BE' : 9.012, 'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999, 'F' : 18.998, 'NE' : 20.180, 'NA' : 22.990, 'MG' : 24.305, 'AL' : 26.982, 'SI' : 28.086, 'P' : 30.974, 'S' : 32.066, 'CL' : 35.453, 'AR' : 39.948, 'K' : 39.098, 'CA' : 40.078, 'SC' : 44.956, 'TI' : 47.867, 'V' : 50.942, 'CR' : 51.996, 'MN' : 54.938, 'FE' : 55.845, 'CO' : 58.933, 'NI' : 58.693, 'CU' : 63.546, 'ZN' : 65.38, 'GA' : 69.723, 'GE' : 72.631, 'AS' : 74.922, 'SE' : 78.971, 'BR' : 79.904, 'KR' : 84.798, 'RB' : 84.468, 'SR' : 87.62, 'Y' : 88.906, 'ZR' : 91.224, 'NB' : 92.906, 'MO' : 95.95, 'TC' : 98.907, 'RU' : 101.07, 'RH' : 102.906, 'PD' : 106.42, 'AG' : 107.868, 'CD' : 112.414, 'IN' : 114.818, 'SN' : 118.711, 'SB' : 121.760, 'TE' : 126.7, 'I' : 126.904, 'XE' : 131.294, 'CS' : 132.905, 'BA' : 137.328, 'LA' : 138.905, 'CE' : 140.116, 'PR' : 140.908, 'ND' : 144.243, 'PM' : 144.913, 'SM' : 150.36, 'EU' : 151.964, 'GD' : 157.25, 'TB' : 158.925, 'DY': 162.500, 'HO' : 164.930, 'ER' : 167.259, 'TM' : 168.934, 'YB' : 173.055, 'LU' : 174.967, 'HF' : 178.49, 'TA' : 180.948, 'W' : 183.84, 'RE' : 186.207, 'OS' : 190.23, 'IR' : 192.217, 'PT' : 195.085, 'AU' : 196.967, 'HG' : 200.592, 'TL' : 204.383, 'PB' : 207.2, 'BI' : 208.980, 'PO' : 208.982, 'AT' : 209.987, 'RN' : 222.081, 'FR' : 223.020, 'RA' : 226.025, 'AC' : 227.028, 'TH' : 232.038, 'PA' : 231.036, 'U' : 238.029, 'NP' : 237, 'PU' : 244}

elements_percentages = {}

print(value_an_object(1000, {"H": .33, "O": .67}))

# explanation and getting input
print("this program finds the chemical value of the object you input. to make this work you'll need:\n- an object\n- its weight\n- the percent composition of each element it is composed of\nif you don't know all of these, please look them up before proceeding.")
next_output = input("\ncontinue? y/n ")
if next_output.lower() == "y":
    while True:
        object_name = input("\nbegin by telling me the name of the object i'll be appraising:\n")
        object_weight = float(input(f"\nalright, how heavy (in grams) is the {object_name} that i'll be appraising?\n"))
        object_elements = input("\ntype out the letter symbols of all the elements in your object, separated by commas.\nfor example, type, \"H, O\" if your object is water. your turn:\n").split(", ")
        print("\nnow you'll be entering what percentage of the object is made up of each element. make sure that these\npercentages are written as decimals less than 1, and the total is exactly 1. otherwise, my answer might not be accurate!")
        for i in object_elements:
            element_percentage = float(input(f"\nwhat percent (as a decimal less than 1) of {object_name} is made up of {i}?\n"))
            elements_percentages[i] = element_percentage
        e_p_string = ""
        if input(f"\nalright, just to check, here's your object again:\n- object: {object_name}\n- weight: {object_weight}\n- elements: {[i for i, j in elements_percentages.items()]}\n- percentages: {[j for i, j in elements_percentages.items()]}\n\n is that all correct? y/n ") == "y":
            break
        else: print("alright, then i suppose we should restart.\n\n\n")
    object_value = value_an_object(object_weight, elements_percentages)
    print(f"\ngreat! the value of your {object_name} is ʇ{object_value}", end="")