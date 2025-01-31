from typing import Dict, Tuple, List
import logging

def extract_topology(atoms_data: Dict[str, Dict]) -> Tuple[Dict, Dict, Dict]:
    """
    Extract bonds, angles, and dihedrals from atom connectivity data with their atom identifiers.
    
    Args:
        atoms_data: Dictionary of atom data from parse_mdf_file()
        
    Returns:
        Tuple of (bond_map, angle_map, dihedral_map) dictionaries
    """
    bonds_set = set()
    bond_map = {}
    angles_set = set()
    angle_map = {}
    dihedrals_set = set()
    dihedral_map = {}

    # Extract bonds
    for atomA, dataA in atoms_data.items():
        groupA = dataA["charge_group"]
        for nbr_label in dataA["neighbors"]:
            if nbr_label not in atoms_data:
                continue
            groupB = atoms_data[nbr_label]["charge_group"]
            bond_tup = tuple(sorted([groupA, groupB]))
            bonds_set.add(bond_tup)
            
            # Store atom identifier pairs for bonds
            bond_key = bond_tup
            if bond_key not in bond_map:
                bond_map[bond_key] = []
            bond_map[bond_key].append(f"{atomA}-{nbr_label}")

    # Extract angles
    for b_label, b_info in atoms_data.items():
        groupB = b_info["charge_group"]
        nbrs = b_info["neighbors"]

        for i in range(len(nbrs)):
            for j in range(i + 1, len(nbrs)):
                a_label, c_label = nbrs[i], nbrs[j]
                if a_label not in atoms_data or c_label not in atoms_data:
                    continue
                groupA = atoms_data[a_label]["charge_group"]
                groupC = atoms_data[c_label]["charge_group"]
                sorted_ends = sorted([groupA, groupC])
                angle_trip = (sorted_ends[0], groupB, sorted_ends[1])
                angles_set.add(angle_trip)

                # Store atom identifier triplets for angles
                if angle_trip not in angle_map:
                    angle_map[angle_trip] = []
                angle_map[angle_trip].append(f"{a_label}-{b_label}-{c_label}")

    # Extract dihedrals
    bond_pairs = set()
    for atomA, dataA in atoms_data.items():
        for nbr in dataA["neighbors"]:
            pair = tuple(sorted([atomA, nbr]))
            bond_pairs.add(pair)

    for bond_pair in bond_pairs:
        b_label, c_label = bond_pair
        if b_label not in atoms_data or c_label not in atoms_data:
            continue

        groupB = atoms_data[b_label]["charge_group"]
        groupC = atoms_data[c_label]["charge_group"]
        neighbors_b = [x for x in atoms_data[b_label]["neighbors"] if x != c_label]
        neighbors_c = [x for x in atoms_data[c_label]["neighbors"] if x != b_label]

        for a_label in neighbors_b:
            if a_label not in atoms_data:
                continue
            groupA = atoms_data[a_label]["charge_group"]

            for d_label in neighbors_c:
                if d_label not in atoms_data or len({a_label, b_label, c_label, d_label}) < 4:
                    continue
                groupD = atoms_data[d_label]["charge_group"]
                forward = (groupA, groupB, groupC, groupD)
                reverse = forward[::-1]
                dihedral_tup = min(forward, reverse)
                dihedrals_set.add(dihedral_tup)

                # Store atom identifier quartets for dihedrals
                if dihedral_tup not in dihedral_map:
                    dihedral_map[dihedral_tup] = []
                dihedral_map[dihedral_tup].append(f"{a_label}-{b_label}-{c_label}-{d_label}")

    logging.debug(f"Extracted {len(bonds_set)} bonds, {len(angles_set)} angles, {len(dihedrals_set)} dihedrals")
    
    return bond_map, angle_map, dihedral_map
