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
    
    in_molecule_section = False
    column_indices = {}
    
    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                    
                # Handle column definitions
                if line.startswith('@column'):
                    parts = line.split()
                    if len(parts) >= 3:
                        col_num = int(parts[1])
                        col_name = parts[2]
                        column_indices[col_name] = col_num - 1
                    continue
                
                # Check for molecule section
                if line.startswith('@molecule'):
                    in_molecule_section = True
                    continue
                
                # Skip comments and headers
                if line.startswith(('!', '#')) or not in_molecule_section:
                    continue
                
                try:
                    # Split on whitespace while preserving quoted strings
                    parts = line.split()
                    if not parts:
                        continue
                    
                    # Store the full atom ID as a string
                    atom_id = parts[0]
                    
                    # Get connections from the last field
                    neighbors = []
                    for part in parts:
                        if part.startswith('C') and len(parts) > parts.index(part) + 1:
                            connections = parts[parts.index(part) + 1].split('/')
                            for conn in connections:
                                if conn != '?' and not conn.isspace():
                                    neighbors.append(conn.strip())
                    
                    # Store atom data
                    atom_type = parts[1] if len(parts) > 1 else ''
                    charge_group = parts[2] if len(parts) > 2 else ''
                    
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
