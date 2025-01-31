#!/usr/bin/env python3

import argparse
import logging
import os
import sys
from rich.console import Console
from parser.mdf_parser import parse_mdf_file
from parser.topology import extract_topology
from parser.output_handler import save_output

console = Console()

def setup_logging(log_file=None):
    """Configure logging based on command line options"""
    log_format = "%(levelname)s: %(message)s"
    if log_file:
        logging.basicConfig(
            level=logging.DEBUG,
            format=log_format,
            filename=log_file,
            filemode='w'
        )
    else:
        logging.basicConfig(level=logging.ERROR, format=log_format)

def main():
    parser = argparse.ArgumentParser(description='Parse MDF files and extract molecular topology.')
    parser.add_argument('input_file', help='Path to the .mdf file')
    parser.add_argument('-o', '--output', default='topology.csv', help='Output file name')
    parser.add_argument('--json', action='store_true', help='Output as JSON instead of CSV')
    parser.add_argument('--separate', action='store_true', help='Save separate files for each component')
    parser.add_argument('--verbose', action='store_true', help='Enable detailed output')
    parser.add_argument('--rich', action='store_true', help='Enable colorized output')
    parser.add_argument('--log', help='Save logs to specified file')

    args = parser.parse_args()

    # Configure logging
    setup_logging(args.log)

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
