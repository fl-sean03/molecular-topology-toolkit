#!/usr/bin/env python3
"""
Unified command-line interface for molecular topology parser tools.
Provides access to MDF and CHARMM parameter file parsing capabilities.
"""

import argparse
import sys
import logging
from .mdf_parser.parser import main as mdf_main
from .charmm_parser.parser import CharmmProcessor, main as charmm_main

def setup_logging(verbose=False, log_file=None):
    """Configure logging based on command line options"""
    log_format = "%(levelname)s: %(message)s"
    level = logging.DEBUG if verbose else logging.ERROR
    if log_file:
        logging.basicConfig(level=level, format=log_format, filename=log_file, filemode='w')
    else:
        logging.basicConfig(level=level, format=log_format)

def main():
    try:
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

        # Parameter Checker
        checker_parser = subparsers.add_parser('check', help='Check parameters between MDF and CHARMM files')
        checker_parser.add_argument('mdf_file', help='Path to the .mdf file')
        checker_parser.add_argument('charmm_file', help='Path to the CHARMM parameter file')
        checker_parser.add_argument('-o', '--output', default='missing_parameters.csv',
                                  help='Output file name')
        checker_parser.add_argument('--json', action='store_true',
                                  help='Output as JSON instead of CSV')
        checker_parser.add_argument('--verbose', action='store_true',
                                  help='Enable detailed output')
        checker_parser.add_argument('--log', help='Save logs to specified file')

        args = parser.parse_args()

        if args.command == 'mdf':
            setup_logging(verbose=args.verbose, log_file=args.log)
            return mdf_main(
                input_file=args.input_file,
                output_file=args.output,
                json_format=args.json,
                separate_files=args.separate,
                verbose=args.verbose,
                log_file=args.log
            )
        elif args.command == 'charmm':
            setup_logging(verbose=args.verbose, log_file=args.log)
            from .charmm_parser.parser import main as charmm_main
            return charmm_main(
                input_file=args.input_file,
                output_dir=args.output_dir,
                json_format=args.json,
                verbose=args.verbose,
                log_file=args.log
            )
        elif args.command == 'check':
            setup_logging(verbose=args.verbose, log_file=args.log)
            from .parameter_checker.parameter_checker import main as checker_main
            return checker_main(
                mdf_file=args.mdf_file,
                charmm_file=args.charmm_file,
                output_file=args.output,
                json_format=args.json,
                verbose=args.verbose,
                log_file=args.log
            )
        else:
            parser.print_help()
            return 1
    
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
