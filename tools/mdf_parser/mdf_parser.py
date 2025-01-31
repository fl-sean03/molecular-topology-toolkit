import logging
from typing import Dict, List, Union

def parse_mdf_file(file_path: str) -> Dict[str, Dict[str, Union[str, List[str]]]]:
    """
    Parse an MDF file and extract atom information.
    
    Args:
        file_path: Path to the MDF file
        
    Returns:
        Dictionary mapping atom IDs to their properties
    """
    atoms_data = {}

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(("!", "#")):
                    continue

                parts = line.split()
                if len(parts) < 12:
                    continue

                atom_id = parts[0]
                charge_group = parts[2]
                neighbors_raw = parts[11:]

                prefix = atom_id.split(":")[0] + ":"
                connections = []
                for token in neighbors_raw:
                    nbr = token.split("/")[0]
                    nbr_full = prefix + nbr if ":" not in nbr else nbr
                    connections.append(nbr_full)
                    
                atoms_data[atom_id] = {
                    "charge_group": charge_group,
                    "neighbors": connections
                }

    except FileNotFoundError:
        raise FileNotFoundError(f"MDF file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading MDF file: {str(e)}")
    
    if not atoms_data:
        raise ValueError("No valid atom data found in the MDF file")
    
    logging.debug(f"Successfully parsed {len(atoms_data)} atoms")
    return atoms_data

def extract_unique_charge_groups(atoms_data: Dict) -> Dict[str, List[str]]:
    """Extract unique force field types (charge groups) and their atom identifiers"""
    charge_group_to_atoms = {}
    for atom_id, info in atoms_data.items():
        charge_group = info["charge_group"]
        if charge_group not in charge_group_to_atoms:
            charge_group_to_atoms[charge_group] = []
        charge_group_to_atoms[charge_group].append(atom_id)
    return charge_group_to_atoms
