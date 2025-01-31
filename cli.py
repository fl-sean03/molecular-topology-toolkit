#!/usr/bin/env python3
"""
Unified command-line interface for molecular topology parser tools.
Provides access to MDF and CHARMM parameter file parsing capabilities.
"""

import argparse
import sys
from parser.mdf_parser import main as mdf_main
from parser.charmm_parser import CharmmProcessor

def charmm_main(args):
    processor = CharmmProcessor()
    processor.process_file(args.input_file, args.output_dir)
    return 0

def main():
    parser = argparse.ArgumentParser(
        description='Molecular topology file parser tools'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Parser commands')
    
    # MDF Parser
    mdf_parser = subparsers.add_parser('mdf', help='Parse MDF files')
    mdf_parser.add_argument('--param', help='Path to CHARMM parameter file')
    mdf_parser.add_argument('input_file', help='Path to the .mdf file')
    mdf_parser.add_argument('-o', '--output', default='topology.csv', 
                           help='Output file name')
    mdf_parser.add_argument('--json', action='store_true',
                           help='Output as JSON instead of CSV')
    mdf_parser.add_argument('--separate', action='store_true',
                           help='Save separate files for each component')
    mdf_parser.add_argument('--verbose', action='store_true',
                           help='Enable detailed output')
    mdf_parser.add_argument('--log', help='Save logs to specified file')

    # CHARMM Parser
    charmm_parser = subparsers.add_parser('charmm', help='Parse CHARMM parameter files')
    charmm_parser.add_argument('input_file', help='Path to CHARMM parameter file')
    charmm_parser.add_argument('-o', '--output_dir', default='.',
                              help='Output directory for parsed files')
    charmm_parser.add_argument('--json', action='store_true',
                              help='Output as JSON instead of CSV')
    charmm_parser.add_argument('--verbose', action='store_true',
                              help='Enable detailed output')
    charmm_parser.add_argument('--log', help='Save logs to specified file')

    args = parser.parse_args()

    if args.command == 'mdf':
        return mdf_main()
    elif args.command == 'charmm':
        return charmm_main(args)
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
#!/usr/bin/env python3
"""
Unified command-line interface for molecular topology parser tools.
Provides access to MDF and CHARMM parameter file parsing capabilities.
"""

import argparse
import sys
from tools.mdf_parser.parser import main as mdf_main
from tools.charmm_parser.parser import CharmmProcessor

def main():
    parser = argparse.ArgumentParser(
        description='Molecular topology file parser tools'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Parser commands')
    
    # MDF Parser
    mdf_parser = subparsers.add_parser('mdf', help='Parse MDF files')
    mdf_parser.add_argument('input_file', help='Path to the .mdf file')
    mdf_parser.add_argument('-o', '--output', default='topology.csv', 
                           help='Output file name')
    mdf_parser.add_argument('--json', action='store_true',
                           help='Output as JSON instead of CSV')
    mdf_parser.add_argument('--separate', action='store_true',
                           help='Save separate files for each component')
    mdf_parser.add_argument('--verbose', action='store_true',
                           help='Enable detailed output')
    mdf_parser.add_argument('--log', help='Save logs to specified file')

    # CHARMM Parser
    charmm_parser = subparsers.add_parser('charmm', help='Parse CHARMM parameter files')
    charmm_parser.add_argument('input_file', help='Path to CHARMM parameter file')
    charmm_parser.add_argument('-o', '--output_dir', default='.',
                              help='Output directory for parsed files')
    charmm_parser.add_argument('--json', action='store_true',
                              help='Output as JSON instead of CSV')
    charmm_parser.add_argument('--verbose', action='store_true',
                              help='Enable detailed output')
    charmm_parser.add_argument('--log', help='Save logs to specified file')

    args = parser.parse_args()

    if args.command == 'mdf':
        return mdf_main()
    elif args.command == 'charmm':
        processor = CharmmProcessor()
        processor.process_file(args.input_file, args.output_dir)
        return 0
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
