#!/usr/bin/env python3

import argparse
import logging
import os
import sys
from rich.console import Console
from .topology import extract_topology
from .output_handler import save_output
from .mdf_parser import parse_mdf_file

console = Console()

def setup_logging(verbose=False, log_file=None):
    """Configure logging based on parameters"""
    log_format = "%(levelname)s: %(message)s"
    level = logging.DEBUG if verbose else logging.ERROR
    if log_file:
        logging.basicConfig(
            level=level,
            format=log_format,
            filename=log_file,
            filemode='w'
        )
    else:
        logging.basicConfig(level=level, format=log_format)

def main(input_file, output_file='topology.csv', json_format=False, separate_files=False, verbose=False, log_file=None):
    """
    Main function for parsing MDF files and extracting molecular topology.
    
    Args:
        input_file: Path to the .mdf file
        output_file: Output file name (default: topology.csv)
        json_format: If True, output as JSON instead of CSV
        separate_files: If True, save separate files for each component
        verbose: Enable detailed output
        log_file: Save logs to specified file
    """
    # Configure logging
    setup_logging(verbose, log_file)

    try:
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
            console.print("[bold blue]Starting MDF file parsing...[/]")

        # Parse the MDF file
        atoms_data = parse_mdf_file(args.input_file)
        
        if args.verbose:
            console.print(f"[green]Successfully parsed {len(atoms_data)} atoms[/]")

        # Extract topology
        bonds, angles, dihedrals = extract_topology(atoms_data)
        
        if args.verbose:
            console.print(f"[green]Extracted topology:[/]")
            console.print(f"  Bonds: {len(bonds)}")
            console.print(f"  Angles: {len(angles)}")
            console.print(f"  Dihedrals: {len(dihedrals)}")

        # Save output
        save_output(
            file_name=args.output,
            atoms_data=atoms_data,
            json_format=args.json,
            separate_files=args.separate
        )

        if args.verbose:
            console.print("[bold green]Processing complete![/]")

    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        if args.verbose:
            console.print(f"[bold red]Error:[/] {str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
