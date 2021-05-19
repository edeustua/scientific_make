import sys
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

ENERGY_RE = re.compile(
    r" +\* CCSD total energy += +(-?\d+\.\d+)"
)

def parse_energy(filename):
    path = Path(filename)
    geometry = float(path.name.replace(".inp.dat", ""))
    if path.exists():
        text = path.read_text()
        for line in text.split("\n"):
            result = ENERGY_RE.match(line)
            if result:
                return geometry, float(result.group(1))
    return geometry, np.nan

files = sys.argv[1:]
data = np.array(list(map(parse_energy, files)))
plt.plot(data[:, 0], data[:, 1])
plt.title(r"Bond dissociation of H$_2$")
plt.xlabel(r"$r_{\rm{H-H}}$ ($\rm{\AA{}}$)")
plt.ylabel(r"Energy ($E_h$)")
plt.tight_layout()
plt.savefig("h2_dissociation.png", format="png", dpi=300)

