import logging
from typing import Dict, List, Union

def parse_mdf_file(file_path: str) -> Dict[int, Dict[str, Union[int, float, List[int]]]]:
    """
    Parse an MDF file and extract atom information.
    
    Args:
        file_path: Path to the MDF file
        
    Returns:
        Dictionary mapping atom IDs to their properties
    """
    atoms_data = {}
    
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith(('!', '#')):
                    continue
                
                try:
                    parts = line.split()
                    if len(parts) < 12:
                        logging.warning(f"Line {line_num}: Insufficient data columns")
                        continue
                    
                    atom_id = int(parts[0])
                    charge_group = int(parts[1])
                    
                    # Extract neighbor information (columns 11 onwards)
                    neighbors = []
                    for neighbor in parts[11:]:
                        if neighbor.startswith(('-', '+')):
                            # Handle periodic boundary conditions
                            neighbor_id = int(neighbor[1:])
                            neighbors.append(neighbor_id)
                        else:
                            neighbors.append(int(neighbor))
                    
                    atoms_data[atom_id] = {
                        'charge_group': charge_group,
                        'neighbors': neighbors
                    }
                    
                except ValueError as e:
                    logging.error(f"Line {line_num}: Error parsing values - {str(e)}")
                    continue
                
    except FileNotFoundError:
        raise FileNotFoundError(f"MDF file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading MDF file: {str(e)}")
    
    if not atoms_data:
        raise ValueError("No valid atom data found in the MDF file")
    
    logging.debug(f"Successfully parsed {len(atoms_data)} atoms")
    return atoms_data
