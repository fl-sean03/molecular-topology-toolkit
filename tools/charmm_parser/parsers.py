"""
CHARMM parameter file section parsers.
Contains functions for parsing different sections of CHARMM parameter files.
"""

import pandas as pd
import re
from typing import List, Dict

def read_file(file_path: str) -> List[str]:
    """Reads the content of a file and returns it as a list of lines."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_bonds_section(lines: List[str], start_line: int = 0) -> pd.DataFrame:
    """Parse the BONDS section of the CHARMM parameter file."""
    parsed_data = []
    current_entry = None
    last_line_was_comment = False
    
    for line_number, line in enumerate(lines, start=start_line):
        line = line.strip()
        
        if not line:
            last_line_was_comment = False
            continue
            
        if line.startswith("!"):
            if current_entry and last_line_was_comment:
                current_entry["Comments"].append(line[1:].strip())
            last_line_was_comment = True
            continue
            
        match = re.match(r"(\S+)\s+(\S+)\s+([\d\.]+)\s+([\d\.]+)(?:\s+!\s*(.*))?", line)
        if match:
            atom1, atom2, kb, b0, initial_comment = match.groups()
            current_entry = {
                "Atom 1": atom1,
                "Atom 2": atom2,
                "Force Constant (Kb)": float(kb),
                "Equilibrium Bond Length (b0)": float(b0),
                "Comments": [initial_comment.strip()] if initial_comment else [],
                "Line Number": line_number,
            }
            parsed_data.append(current_entry)
            last_line_was_comment = True
            
    return pd.DataFrame(parsed_data)

def parse_angles_section(lines: List[str], start_line: int = 0) -> pd.DataFrame:
    """Parse the ANGLES section of the CHARMM parameter file."""
    parsed_data = []
    current_entry = None
    last_line_was_comment = False
    
    for line_number, line in enumerate(lines, start=start_line):
        line = line.strip()
        
        if not line:
            last_line_was_comment = False
            continue
            
        if line.startswith("!"):
            if current_entry and last_line_was_comment:
                current_entry["Comments"].append(line[1:].strip())
            last_line_was_comment = True
            continue
            
        match = re.match(
            r"(\S+)\s+(\S+)\s+(\S+)\s+([\d\.]+)\s+([\d\.]+)(?:\s+([\d\.]+))?(?:\s+([\d\.]+))?(?:\s+!\s*(.*))?",
            line
        )
        if match:
            atom1, atom2, atom3, ktheta, theta0, kub, s0, initial_comment = match.groups()
            current_entry = {
                "Atom 1": atom1,
                "Atom 2": atom2,
                "Atom 3": atom3,
                "Ktheta": float(ktheta),
                "Theta0 (Equilibrium Angle)": float(theta0),
                "Kub": float(kub) if kub else None,
                "S0": float(s0) if s0 else None,
                "Comments": [initial_comment.strip()] if initial_comment else [],
                "Line Number": line_number,
            }
            parsed_data.append(current_entry)
            last_line_was_comment = True
            
    return pd.DataFrame(parsed_data)

def parse_dihedrals_section(lines: List[str], start_line: int = 0) -> pd.DataFrame:
    """Parse the DIHEDRALS section of the CHARMM parameter file."""
    parsed_data = []
    current_entry = None
    last_line_was_comment = False
    
    for line_number, line in enumerate(lines, start=start_line):
        line = line.strip()
        
        if not line:
            last_line_was_comment = False
            continue
            
        if line.startswith("!"):
            if current_entry and last_line_was_comment:
                current_entry["Comments"].append(line[1:].strip())
            last_line_was_comment = True
            continue
            
        match = re.match(
            r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([\d\.]+)\s+(\d+)\s+([\d\.]+)(?:\s+!\s*(.*))?",
            line
        )
        if match:
            atom1, atom2, atom3, atom4, kchi, multiplicity, delta, initial_comment = match.groups()
            current_entry = {
                "Atom 1": atom1,
                "Atom 2": atom2,
                "Atom 3": atom3,
                "Atom 4": atom4,
                "Kchi": float(kchi),
                "Multiplicity (n)": int(multiplicity),
                "Delta": float(delta),
                "Comments": [initial_comment.strip()] if initial_comment else [],
                "Line Number": line_number,
            }
            parsed_data.append(current_entry)
            last_line_was_comment = True
            
    return pd.DataFrame(parsed_data)

def parse_impropers_section(lines: List[str], start_line: int = 0) -> pd.DataFrame:
    """Parse the IMPROPER section of the CHARMM parameter file."""
    parsed_data = []
    current_entry = None
    last_line_was_comment = False
    
    for line_number, line in enumerate(lines, start=start_line):
        line = line.strip()
        
        if not line:
            last_line_was_comment = False
            continue
            
        if line.startswith("!"):
            if current_entry and last_line_was_comment:
                current_entry["Comments"].append(line[1:].strip())
            last_line_was_comment = True
            continue
            
        match = re.match(
            r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([-\d\.]+)\s+\d+\s+([\d\.]+)(?:\s+!\s*(.*))?",
            line
        )
        if match:
            atom1, atom2, atom3, atom4, kpsi, psi0, initial_comment = match.groups()
            current_entry = {
                "Atom 1": atom1,
                "Atom 2": atom2,
                "Atom 3": atom3,
                "Atom 4": atom4,
                "Kpsi": float(kpsi),
                "Psi0": float(psi0),
                "Comments": [initial_comment.strip()] if initial_comment else [],
                "Line Number": line_number,
            }
            parsed_data.append(current_entry)
            last_line_was_comment = True
            
    return pd.DataFrame(parsed_data)

def parse_atoms_section(lines: List[str], start_line: int = 0) -> pd.DataFrame:
    """Parse the ATOMS section of the CHARMM parameter file."""
    parsed_data = []
    current_entry = None
    last_line_was_comment = False
    
    for line_number, line in enumerate(lines, start=start_line):
        line = line.strip()
        
        if not line:
            last_line_was_comment = False
            continue
            
        if line.startswith("!"):
            if current_entry and last_line_was_comment:
                current_entry["Comments"].append(line[1:].strip())
            last_line_was_comment = True
            continue
            
        match = re.match(r"MASS\s+-?\d+\s+(\S+)\s+([\d\.]+)(?:\s+!\s*(.*))?", line)
        if match:
            atom_type, mass, initial_comment = match.groups()
            current_entry = {
                "Force Field Type": atom_type,
                "Mass": float(mass),
                "Comments": [initial_comment.strip()] if initial_comment else [],
                "Line Number": line_number,
            }
            parsed_data.append(current_entry)
            last_line_was_comment = True
            
    return pd.DataFrame(parsed_data)

def parse_charmm_parameter_file(filepath: str) -> Dict[str, pd.DataFrame]:
    """
    Parse a full CHARMM parameter file into individual sections while preserving global line numbers.
    """
    # Read the file
    lines = read_file(filepath)
    
    # Define section patterns
    section_patterns = {
        "ATOMS": r"^ATOMS",
        "BONDS": r"^BONDS",
        "ANGLES": r"^ANGLES",
        "DIHEDRALS": r"^DIHEDRALS",
        "IMPROPER": r"^IMPROPER",
        "CMAP": r"^CMAP",
    }
    
    # Locate sections
    sections = {}
    current_section = None
    section_lines = []
    current_start_line = 0
    
    for i, line in enumerate(lines):
        # Check for section headers
        for section_name, pattern in section_patterns.items():
            if re.match(pattern, line.strip(), re.IGNORECASE):
                # Save the previous section
                if current_section and section_lines:
                    sections[current_section] = {
                        "lines": section_lines,
                        "start_line": current_start_line,
                    }
                # Start a new section
                current_section = section_name
                section_lines = []
                current_start_line = i + 1
                break
        else:
            # Accumulate lines for the current section
            if current_section:
                section_lines.append(line.strip())
    
    # Save the last section
    if current_section and section_lines:
        sections[current_section] = {
            "lines": section_lines,
            "start_line": current_start_line,
        }
    
    # Parse sections using corresponding parsers
    parsed_data = {}
    for section_name, section_data in sections.items():
        section_lines = section_data["lines"]
        start_line = section_data["start_line"]
        
        if section_name == "ATOMS":
            parsed_data["ATOMS"] = parse_atoms_section(section_lines, start_line+1)
        elif section_name == "BONDS":
            parsed_data["BONDS"] = parse_bonds_section(section_lines, start_line+1)
        elif section_name == "ANGLES":
            parsed_data["ANGLES"] = parse_angles_section(section_lines, start_line+1)
        elif section_name == "DIHEDRALS":
            parsed_data["DIHEDRALS"] = parse_dihedrals_section(section_lines, start_line+1)
        elif section_name == "IMPROPER":
            parsed_data["IMPROPER"] = parse_impropers_section(section_lines, start_line+1)
    
    return parsed_data
