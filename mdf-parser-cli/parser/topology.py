from typing import Dict, Set, Tuple, List
import logging

def extract_topology(atoms_data: Dict[int, Dict]) -> Dict[str, Set[Tuple]]:
    """
    Extract bonds, angles, and dihedrals from atom connectivity data.
    
    Args:
        atoms_data: Dictionary of atom data from parse_mdf_file()
        
    Returns:
        Dictionary containing sets of bonds, angles, and dihedrals
    """
    bonds = set()
    angles = set()
    dihedrals = set()
    
    # Extract bonds
    for atom_id, data in atoms_data.items():
        atom_group = data['charge_group']
        for neighbor in data['neighbors']:
            if neighbor in atoms_data:
                neighbor_group = atoms_data[neighbor]['charge_group']
                bond = tuple(sorted([atom_group, neighbor_group]))
                bonds.add(bond)
    
    # Extract angles
    for atom_id, data in atoms_data.items():
        if len(data['neighbors']) >= 2:
            center_group = data['charge_group']
            neighbors = data['neighbors']
            
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    if neighbors[i] in atoms_data and neighbors[j] in atoms_data:
                        group1 = atoms_data[neighbors[i]]['charge_group']
                        group2 = atoms_data[neighbors[j]]['charge_group']
                        angle = (group1, center_group, group2)
                        angles.add(angle)
    
    # Extract dihedrals (optional)
    # Implementation for dihedrals can be added here if needed
    
    logging.debug(f"Extracted {len(bonds)} bonds, {len(angles)} angles, {len(dihedrals)} dihedrals")
    
    return {
        'bonds': bonds,
        'angles': angles,
        'dihedrals': dihedrals
    }
