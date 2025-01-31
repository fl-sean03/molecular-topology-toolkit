import json
import os
import pandas as pd
import logging
from typing import Dict, Set, Tuple

def save_output(
    file_name: str,
    atoms: Dict,
    topology: Dict[str, Set[Tuple]],
    json_format: bool = False,
    separate_files: bool = False
) -> None:
    """
    Save parsed data to output files in CSV or JSON format.
    
    Args:
        file_name: Base name for output file(s)
        atoms: Dictionary of atom data
        topology: Dictionary containing bonds, angles, and dihedrals
        json_format: If True, save as JSON instead of CSV
        separate_files: If True, save each component to a separate file
    """
    base_name = os.path.splitext(file_name)[0]
    
    # Convert atom data to DataFrame
    atoms_df = pd.DataFrame.from_dict(atoms, orient='index')
    
    # Convert topology components to DataFrames
    bonds_df = pd.DataFrame(list(topology['bonds']), columns=['Atom1', 'Atom2'])
    angles_df = pd.DataFrame(list(topology['angles']), columns=['Atom1', 'Atom2', 'Atom3'])
    dihedrals_df = pd.DataFrame(list(topology['dihedrals']), columns=['Atom1', 'Atom2', 'Atom3', 'Atom4'])
    
    if json_format:
        output_data = {
            'atoms': atoms_df.to_dict(orient='index'),
            'bonds': bonds_df.to_dict(orient='records'),
            'angles': angles_df.to_dict(orient='records'),
            'dihedrals': dihedrals_df.to_dict(orient='records')
        }
        
        with open(f"{base_name}.json", 'w') as f:
            json.dump(output_data, f, indent=2)
        logging.info(f"Saved JSON output to {base_name}.json")
        
    elif separate_files:
        atoms_df.to_csv(f"{base_name}_atoms.csv")
        bonds_df.to_csv(f"{base_name}_bonds.csv", index=False)
        angles_df.to_csv(f"{base_name}_angles.csv", index=False)
        dihedrals_df.to_csv(f"{base_name}_dihedrals.csv", index=False)
        logging.info(f"Saved separate CSV files with base name {base_name}")
        
    else:
        # Combine all data into a single CSV with sections
        with open(file_name, 'w') as f:
            f.write("# Atoms\n")
            atoms_df.to_csv(f)
            f.write("\n# Bonds\n")
            bonds_df.to_csv(f, index=False)
            f.write("\n# Angles\n")
            angles_df.to_csv(f, index=False)
            f.write("\n# Dihedrals\n")
            dihedrals_df.to_csv(f, index=False)
        logging.info(f"Saved combined CSV output to {file_name}")
