import json
import os
import pandas as pd
import logging
from typing import Dict, List, Tuple
from .mdf_parser import extract_unique_charge_groups

def generate_topology_dataframe(atoms_data: Dict) -> pd.DataFrame:
    """
    Generate a unified DataFrame containing all topology information.
    
    Args:
        atoms_data: Dictionary of atom data from parse_mdf_file()
        
    Returns:
        DataFrame with columns: record_type, atom_identifiers, data1, data2, data3, data4
    """
    from .topology import extract_topology
    
    charge_group_to_atoms = extract_unique_charge_groups(atoms_data)
    bond_map, angle_map, dihedral_map = extract_topology(atoms_data)

    data = []

    # Unique Charge Groups (Atoms)
    for charge_group, atom_list in charge_group_to_atoms.items():
        data.append(["atom", atom_list, charge_group, "", "", ""])

    # Bonds
    for (g1, g2), bond_list in bond_map.items():
        data.append(["bond", bond_list, g1, g2, "", ""])

    # Angles
    for (g1, g2, g3), angle_list in angle_map.items():
        data.append(["angle", angle_list, g1, g2, g3, ""])

    # Dihedrals
    for (g1, g2, g3, g4), dihedral_list in dihedral_map.items():
        data.append(["dihedral", dihedral_list, g1, g2, g3, g4])

    return pd.DataFrame(data, columns=["record_type", "atom_identifiers", "data1", "data2", "data3", "data4"])

def save_output(
    file_name: str,
    atoms_data: Dict,
    json_format: bool = False,
    separate_files: bool = False
) -> None:
    """
    Save parsed data to output files in CSV or JSON format.
    
    Args:
        file_name: Base name for output file(s)
        atoms_data: Dictionary of atom data from parse_mdf_file()
        json_format: If True, save as JSON instead of CSV
        separate_files: If True, save each component to a separate file
    """
    base_name = os.path.splitext(file_name)[0]
    df_final = generate_topology_dataframe(atoms_data)
    
    if json_format:
        output_data = df_final.to_dict(orient='records')
        with open(f"{base_name}.json", 'w') as f:
            json.dump(output_data, f, indent=2)
        logging.info(f"Saved JSON output to {base_name}.json")
        
    elif separate_files:
        for record_type in ['atom', 'bond', 'angle', 'dihedral']:
            subset = df_final[df_final['record_type'] == record_type]
            if not subset.empty:
                subset.to_csv(f"{base_name}_{record_type}s.csv", index=False)
        logging.info(f"Saved separate CSV files with base name {base_name}")
        
    else:
        df_final.to_csv(file_name, index=False)
        logging.info(f"Saved combined CSV output to {file_name}")
