# Nuclear Fusion Reaction Data

This directory contains data for nuclear fusion reaction channels.
Each reaction is stored in a directory whose name identifies its reactants and products.
For example, `D_d_n_He3` represents the reaction $D(d,n){}^{3}He$.

## Angular distribution coefficients

Angular distribution coefficient tables are located at `<reaction>/angular_distribution/<format>/coefficients.txt`, where `<format>` is either `endf` or `iaea`.
Each row has the following form:

```text
E L0 L1 ... L16
```

The `iaea` coefficients are based on the [IAEA evaluated nuclear-data records](https://www-nds.iaea.org/records/t5vy7-v2d27), in particular Table 2.2 for $D(d,n){}^{3}He$ and Table 3.2 for $T(d,n){}^{4}He$.
They are denoted by $A_l$ in the IAEA records and by $L_l$ in the data files.

The `endf` coefficients are obtained by converting the IAEA coefficients to the ENDF orthonormal Legendre convention.

For each Legendre order $l$, the IAEA coefficients are converted as follows:

$$
L_l^{\mathrm{ENDF}} =
\frac{A_l^{\mathrm{IAEA}} / A_0^{\mathrm{IAEA}}}{2l + 1}.
$$

The coefficient convention is documented in [ENDF-102 (2023)](https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf).

Both formats contain center-of-mass energies in the first column, `E`.
The original energy values in the IAEA records are not center-of-mass energies and were converted before being included in these tables.
