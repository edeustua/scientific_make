# Scientific Make Tutorial
This repository holds a small presentation and example files for a tutorial on
how to use `make` to drive scientific computations.

The `examples` folder holds the `pes` which is meant to show the capabilities
of `make`. To run this example you will need the following software:

1. `psi4`: you can easily install it using anaconda with
   ```bash
   $ conda install psi4=1.4rc1 psi4-rt=1.4.dev30 python=3.8 -c psi4/label/dev
   ```
2. `python`
3. `numpy`
4. `matplotlib`

Once these dependencies are satisfied, one can proceed to build the input files
using,
```bash
$ cd examples/pes
$ python3 generate_inputs.py
```
and drive the calculations by simply calling make,
```bash
$ make
```

The result should be a file named `h2_dissociation.png` which should look like this
![PES plot](/latex/h2_dissociation.png).
