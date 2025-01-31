"""
Main module for parameter checking functionality.
Compares parameters between MDF and CHARMM parameter files.
"""

import logging
from typing import Dict, Set, Tuple, List
import json
import pandas as pd
from rich.console import Console
from ..mdf_parser.mdf_parser import parse_mdf_file, extract_unique_charge_groups
from ..mdf_parser.topology import extract_topology
from ..charmm_parser.parsers import parse_charmm_parameter_file

console = Console()

def compare_atoms(mdf_atoms: Set[str], charmm_atoms: Set[str]) -> Set[str]:
    """Compare atom types between MDF and CHARMM data."""
    return mdf_atoms - charmm_atoms

def compare_parameters(mdf_params: Dict, charmm_params: Dict) -> Set[Tuple]:
    """Compare parameter tuples between MDF and CHARMM data."""
    return set(mdf_params.keys()) - set(charmm_params.keys())

def save_results(results: Dict, output_file: str, json_format: bool = False) -> None:
    """Save comparison results to file in CSV or JSON format."""
    if json_format:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
    else:
        rows = []
        for param_type, missing in results.items():
            if param_type == 'atoms':
                rows.extend([('atom', atom) for atom in missing])
            else:
                rows.extend([(param_type[:-1], '-'.join(param)) for param in missing])
        
        df = pd.DataFrame(rows, columns=['parameter_type', 'parameters'])
        df.to_csv(output_file, index=False)

def main(
    mdf_file: str,
    charmm_file: str,
    output_file: str = 'missing_parameters.csv',
    json_format: bool = False,
    verbose: bool = False,
    log_file: str = None
) -> int:
    """
    Main function for comparing parameters between MDF and CHARMM files.
    
    Args:
        mdf_file: Path to the MDF file
        charmm_file: Path to the CHARMM parameter file
        output_file: Output file name
        json_format: If True, output as JSON instead of CSV
        verbose: Enable detailed output
        log_file: Save logs to specified file
        
    Returns:
        0 on success, 1 on error
    """
    try:
        if verbose:
            console.print("[bold blue]Starting parameter comparison...[/]")
            console.print(f"[blue]MDF file:[/] {mdf_file}")
            console.print(f"[blue]CHARMM file:[/] {charmm_file}")
        
        # Parse MDF file
        logging.info("Parsing MDF file...")
        atoms_data = parse_mdf_file(mdf_file)
        mdf_atoms = set(extract_unique_charge_groups(atoms_data).keys())
        bond_map, angle_map, dihedral_map = extract_topology(atoms_data)
        
        # Normalize MDF angles
        mdf_angles = set()
        for angle in angle_map.keys():
            A, B, C = angle
            normalized_angle = (min(A, C), B, max(A, C))
            mdf_angles.add(normalized_angle)
            
        # Normalize MDF dihedrals
        mdf_dihedrals = set()
        for dihedral in dihedral_map.keys():
            dihedral_forward = dihedral
            dihedral_reverse = dihedral[::-1]
            normalized_dihedral = min(dihedral_forward, dihedral_reverse)
            mdf_dihedrals.add(normalized_dihedral)
        
        if verbose:
            console.print(f"[green]Found in MDF:[/]")
            console.print(f"  Atoms: {len(mdf_atoms)}")
            console.print(f"  Bonds: {len(bond_map)}")
            console.print(f"  Angles: {len(angle_map)}")
            console.print(f"  Dihedrals: {len(dihedral_map)}")
        
        # Parse CHARMM file
        logging.info("Parsing CHARMM parameter file...")
        charmm_data = parse_charmm_parameter_file(charmm_file)
        
        # Extract CHARMM parameters
        charmm_atoms = set(charmm_data['ATOMS']['Force Field Type'].unique()) if 'ATOMS' in charmm_data else set()
        
        # Extract and normalize bonds (already normalized by sorting)
        charmm_bonds = {tuple(sorted([row['Atom 1'], row['Atom 2']])) 
                       for _, row in charmm_data.get('BONDS', pd.DataFrame()).iterrows()}
        
        # Extract and normalize angles
        charmm_angles = set()
        angles_df = charmm_data.get('ANGLES', pd.DataFrame())
        for _, row in angles_df.iterrows():
            A = row['Atom 1']
            B = row['Atom 2']
            C = row['Atom 3']
            normalized_angle = (min(A, C), B, max(A, C))
            charmm_angles.add(normalized_angle)
            
        # Extract and normalize dihedrals
        charmm_dihedrals = set()
        dihedrals_df = charmm_data.get('DIHEDRALS', pd.DataFrame())
        for _, row in dihedrals_df.iterrows():
            A = row['Atom 1']
            B = row['Atom 2']
            C = row['Atom 3']
            D = row['Atom 4']
            dihedral = (A, B, C, D)
            reversed_dihedral = dihedral[::-1]
            normalized_dihedral = min(dihedral, reversed_dihedral)
            charmm_dihedrals.add(normalized_dihedral)
        
        if verbose:
            console.print(f"[green]Found in CHARMM:[/]")
            console.print(f"  Atoms: {len(charmm_atoms)}")
            console.print(f"  Bonds: {len(charmm_bonds)}")
            console.print(f"  Angles: {len(charmm_angles)}")
            console.print(f"  Dihedrals: {len(charmm_dihedrals)}")
        
        # Compare parameters
        missing_atoms = compare_atoms(mdf_atoms, charmm_atoms)
        missing_bonds = compare_parameters(bond_map, charmm_bonds)
        missing_angles = mdf_angles - charmm_angles
        missing_dihedrals = mdf_dihedrals - charmm_dihedrals
        
        results = {
            'atoms': list(missing_atoms),
            'bonds': [list(bond) for bond in missing_bonds],
            'angles': [list(angle) for angle in missing_angles],
            'dihedrals': [list(dihedral) for dihedral in missing_dihedrals]
        }
        
        # Save results
        save_results(results, output_file, json_format)
        
        if verbose:
            console.print("\n[bold green]Missing Parameters:[/]")
            for param_type, missing in results.items():
                console.print(f"[cyan]{param_type}:[/] {len(missing)}")
            console.print(f"\n[bold green]Results saved to {output_file} ✓[/]")
        
        return 0
        
    except Exception as e:
        logging.error(f"Error comparing parameters: {str(e)}")
        if verbose:
            console.print(f"[bold red]Error:[/] {str(e)}")
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
