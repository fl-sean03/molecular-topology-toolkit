"""
CHARMM parameter file parser main module.
Provides the CharmmProcessor class and main function for handling CHARMM parameter files.
"""

import sys
import logging
from typing import Dict, List, Optional
from rich.console import Console
import os
import pandas as pd
from .parsers import parse_charmm_parameter_file

class CharmmProcessor:
    def __init__(self):
        self.current_data: Dict[str, pd.DataFrame] = {}
        self.filepath: Optional[str] = None

    def process_file(self, filepath: str, output_dir: str) -> Dict[str, pd.DataFrame]:
        """Process a CHARMM parameter file and store results"""
        logging.info(f"Processing CHARMM parameter file: {filepath}")
        self.filepath = filepath
        self.current_data = parse_charmm_parameter_file(filepath)
        
        # Save each section to a CSV file in the output directory
        logging.info(f"Saving parsed data to: {output_dir}")
        for section_name, df in self.current_data.items():
            if not df.empty:
                output_path = os.path.join(output_dir, f'{section_name}.csv')
                df.to_csv(output_path, index=False)
                logging.debug(f"Saved {section_name} section with {len(df)} entries to {output_path}")
        
        return self.current_data



def main(input_file: str, output_dir: str = '.', json_format: bool = False, verbose: bool = False, log_file: Optional[str] = None) -> int:
    """
    Main function for parsing CHARMM parameter files.
    
    Args:
        input_file: Path to the CHARMM parameter file
        output_dir: Output directory for parsed files
        json_format: If True, output as JSON instead of CSV
        verbose: Enable detailed output
        log_file: Save logs to specified file
        
    Returns:
        0 on success, 1 on error
    """
    console = Console()
    
    try:
        if verbose:
            logging.getLogger().setLevel(logging.DEBUG)
            console.print("[bold blue]Starting CHARMM parameter file parsing...[/]")
            console.print(f"[blue]Input file:[/] {input_file}")
            console.print(f"[blue]Output directory:[/] {output_dir}")
            console.print(f"[blue]Output format:[/] {'JSON' if json_format else 'CSV'}")
        
        processor = CharmmProcessor()
        data = processor.process_file(input_file, output_dir)
        
        if json_format:
            console.print("[yellow]Converting to JSON format...[/]")
            for section, df in data.items():
                output_path = os.path.join(output_dir, f'{section}.json')
                df.to_json(output_path, orient='records', indent=2)
                if verbose:
                    console.print(f"[green]  Saved {section}.json[/]")
        
        if verbose:
            console.print("\n[bold green]Parsing Summary:[/]")
            console.print(f"[green]Successfully parsed {len(data)} sections:[/]")
            for section, df in data.items():
                console.print(f"  [cyan]{section}:[/] {len(df)} entries")
                if not df.empty:
                    console.print(f"    Columns: {', '.join(df.columns)}")
            console.print("\n[bold green]Processing complete! ✓[/]")
            
        return 0
        
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        if verbose:
            console.print(f"[bold red]Error:[/] {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
