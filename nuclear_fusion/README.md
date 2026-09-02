# Nuclear Fusion Reaction Data

This directory contains data for nuclear fusion reaction channels. Each reaction is stored in a
directory whose name identifies its reactants and products. For example, `D_d_n_He3` represents
the reaction $D(d,n){}^3\mathrm{He}$.

## Angular-distribution coefficients

Angular-distribution coefficient tables are located at
`<reaction>/angular_distribution/endf/coefficients.txt`. Each row contains a center-of-mass energy
followed by the corresponding ENDF orthonormal Legendre coefficients:

```text
E A0 A1 ... A16
```

The coefficients are derived from the
[IAEA evaluated nuclear-data records](https://www-nds.iaea.org/records/t5vy7-v2d27).

For each Legendre order $l$, the IAEA coefficients are converted as follows:

$$
A_l^{\mathrm{ENDF}} =
\frac{A_l^{\mathrm{IAEA}} / A_0^{\mathrm{IAEA}}}{2l + 1}.
$$

The coefficient convention is documented in
[ENDF-102 (2023)](https://www.nndc.bnl.gov/endfdocs/ENDF-102-2023.pdf).
