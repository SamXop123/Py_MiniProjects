
# Bond Length and Bond Angle calculator
# Using coordinate input of the atoms within the molecule

import math

#Calculating bond length
def bond_length(atom1, atom2):
    return math.sqrt((atom2[0] - atom1[0])**2 +
                     (atom2[1] - atom1[1])**2 +
                     (atom2[2] - atom1[2])**2)

#Calculating bond angle
def bond_angle(atom1, atom2, atom3):

    vector_a = [atom2[0] - atom1[0], atom2[1] - atom1[1], atom2[2] - atom1[2]]
    vector_b = [atom2[0] - atom3[0], atom2[1] - atom3[1], atom2[2] - atom3[2]]

    #Dot product and magnitudes
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a**2 for a in vector_a))
    magnitude_b = math.sqrt(sum(b**2 for b in vector_b))

    #Dot Product to find angle in radians
    angle_radians = math.acos(dot_product / (magnitude_a * magnitude_b))
    #Conversion to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

print("Enter coordinates of Atom 1 (x, y, z):")
atom1 = tuple(map(float, input().split()))
print("Enter coordinates of Atom 2 (x, y, z):")
atom2 = tuple(map(float, input().split()))
print("Enter coordinates of Atom 3 (x, y, z):")
atom3 = tuple(map(float, input().split()))

bond_length_1_2 = bond_length(atom1, atom2)
bond_length_2_3 = bond_length(atom2, atom3)
bond_angle_123 = bond_angle(atom1, atom2, atom3)

print(f"Bond length between Atom 1 and Atom 2: {bond_length_1_2:.3f} Å")
print(f"Bond length between Atom 2 and Atom 3: {bond_length_2_3:.3f} Å")
print(f"Bond angle at Atom 2 (Atoms 1-2-3): {bond_angle_123:.2f} degrees")
