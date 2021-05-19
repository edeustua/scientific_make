from pathlib import Path
import numpy as np

# PSI4 RHF-CCSD input template
TEMPLATE = """
molecule h2 {{
H
H 1 {length}
}}

set basis cc-pVDZ
set freeze_core True
energy('CCSD')
"""

# Linear range from 0.2 to 5 angstrom
length_range = np.linspace(0.2, 5, 100)

if not Path("inputs").exists():
    Path("inputs").mkdir()

# Write input files
for length in length_range:
    input_filename = f"inputs/{length:04.4f}.inp"
    Path(input_filename).write_text(TEMPLATE.format(length=length))
