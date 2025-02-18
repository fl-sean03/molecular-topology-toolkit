"""
Main module for parameter checking functionality.
Compares parameters between MDF and CHARMM parameter files.
"""

import logging
import os
from typing import Dict, Set, Tuple, List
import json
import pandas as pd
from rich.console import Console
from ..mdf_parser.mdf_parser import parse_mdf_file, extract_unique_charge_groups
from ..mdf_parser.topology import extract_topology
from ..charmm_parser.parsers import parse_charmm_parameter_file

console = Console()

def compare_atoms(mdf_atoms: Set[str], charmm_atoms: Set[str], charmm_data: pd.DataFrame) -> List[Dict]:
    """Compare atom types between MDF and CHARMM data."""
    results = []
    for atom in mdf_atoms:
        match = charmm_data[charmm_data['Force Field Type'] == atom]
        results.append({
            'parameter_type': 'atom',
            'parameters': atom,
            'found': not match.empty,
            'line_number': int(match['Line Number'].iloc[0]) if not match.empty else None
        })
    return results

def compare_parameters(mdf_params: Dict, charmm_params: Dict, charmm_df: pd.DataFrame, param_type: str) -> List[Dict]:
    """
    Compare parameter tuples between MDF and CHARMM data, handling wildcards ('X').
    
    Args:
        mdf_params: Dictionary of parameters from MDF file
        charmm_params: Dictionary of parameters from CHARMM file
        charmm_df: DataFrame containing CHARMM parameters
        param_type: Type of parameter being compared ('bond', 'angle', etc.)
        
    Returns:
        List of dictionaries containing comparison results
    """
    if not mdf_params or not charmm_params:
        logging.warning(f"Empty parameter set for {param_type} comparison")
        return []
        
    results = []
    for param_key in mdf_params.keys():
        param_str = '-'.join(param_key)
        found = False
        line_number = None
        
        if not all(isinstance(x, str) for x in param_key):
            logging.warning(f"Invalid parameter key format: {param_key}")
            continue
        
        # Generate all possible orientations based on parameter type
        orientations = []
        if param_type == 'bond':
            # Bonds: A-B or B-A
            orientations = [param_key, param_key[::-1]]
        elif param_type == 'angle':
            # Angles: A-B-C or C-B-A (B must stay in middle)
            orientations = [param_key, (param_key[2], param_key[1], param_key[0])]
        elif param_type == 'dihedral':
            # Dihedrals: A-B-C-D or D-C-B-A
            orientations = [param_key, param_key[::-1]]
        elif param_type == 'improper':
            # Impropers: A-B-C-D, where B is the central atom
            # All permutations of A,C,D around B are equivalent
            from itertools import permutations
            central = param_key[1]  # B is central
            others = [param_key[0], param_key[2], param_key[3]]
            orientations = [(a, central, b, c) for a, b, c in permutations(others)]
        
        # Try all valid orientations
        for orientation in orientations:
            # Create conditions that match either the exact atom type or 'X'
            conditions = []
            for i, atom in enumerate(orientation):
                atom_col = f'Atom {i+1}'
                # Match either the exact atom type or 'X'
                conditions.append(
                    (charmm_df[atom_col] == atom) | (charmm_df[atom_col] == 'X')
                )
            
            # Find matches considering wildcards
            match = charmm_df[pd.concat(conditions, axis=1).all(axis=1)]
            
            if not match.empty:
                found = True
                line_number = int(match['Line Number'].iloc[0])
                break
        
        results.append({
            'parameter_type': param_type,
            'parameters': param_str,
            'found': found,
            'line_number': line_number
        })
    return results

def save_results(results: List[Dict], output_file: str, json_format: bool = False) -> None:
    """Save comparison results to file in CSV or JSON format."""
    if json_format:
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
    else:
        df = pd.DataFrame(results)
        df.to_csv(output_file, index=False)

def main(
    mdf_file: str,
    charmm_file: str, 
    output_file: str = 'parameter_check.csv',
    output_dir: str = '.',
    save_all: bool = False,
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
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, output_file)

        if verbose:
            console.print("[bold blue]Starting parameter comparison...[/]")
            console.print(f"[blue]Output directory:[/] {output_dir}")
            console.print(f"[blue]MDF file:[/] {mdf_file}")
            console.print(f"[blue]CHARMM file:[/] {charmm_file}")
        
        # Parse MDF file and optionally save results
        logging.info("Parsing MDF file...")
        mdf_output = os.path.join(output_dir, 'mdf_topology.csv') if save_all else None
        atoms_data = parse_mdf_file(mdf_file)
        if save_all:
            from ..mdf_parser.output_handler import save_output
            save_output(mdf_output, atoms_data, json_format=json_format)
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
        
        # Parse CHARMM file and optionally save results
        logging.info("Parsing CHARMM parameter file...")
        charmm_output_dir = os.path.join(output_dir, 'charmm') if save_all else None
        if save_all:
            os.makedirs(charmm_output_dir, exist_ok=True)
        charmm_data = parse_charmm_parameter_file(charmm_file)
        if save_all:
            from ..charmm_parser.parser import CharmmProcessor
            processor = CharmmProcessor()
            processor.process_file(charmm_file, charmm_output_dir, json_format=json_format)
        
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
        results = []
        
        # Check atoms
        atom_results = compare_atoms(mdf_atoms, charmm_atoms, charmm_data['ATOMS'])
        results.extend(atom_results)
        
        # Check bonds
        bond_results = compare_parameters(bond_map, charmm_bonds, charmm_data['BONDS'], 'bond')
        results.extend(bond_results)
        
        # Check angles
        angle_results = compare_parameters(angle_map, charmm_angles, charmm_data['ANGLES'], 'angle')
        results.extend(angle_results)
        
        # Check dihedrals
        dihedral_results = compare_parameters(dihedral_map, charmm_dihedrals, charmm_data['DIHEDRALS'], 'dihedral')
        results.extend(dihedral_results)
        
        # Save results
        save_results(results, output_file, json_format)
        
        if verbose:
            found = sum(1 for r in results if r['found'])
            not_found = sum(1 for r in results if not r['found'])
            
            console.print("\n[bold green]Results Summary:[/]")
            console.print(f"Parameters found: {found}")
            console.print(f"Parameters not found: {not_found}")
            
            # Display found parameters
            if found > 0:
                console.print("\n[bold cyan]Found Parameters:[/]")
                for r in results:
                    if r['found']:
                        console.print(f"  [green]{r['parameter_type'].upper()}:[/] {r['parameters']} [dim](line {r['line_number']})[/]")
            
            # Display missing parameters
            if not_found > 0:
                console.print("\n[bold red]Missing Parameters:[/]")
                for r in results:
                    if not r['found']:
                        console.print(f"  [yellow]{r['parameter_type'].upper()}:[/] {r['parameters']}")
            
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
