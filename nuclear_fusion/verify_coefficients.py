#!/usr/bin/env python3
from pathlib import Path

import numpy as np

tol = 10 * np.finfo(float).eps
for path in Path(__file__).parent.glob("*/angular_distribution/endf/coefficients.txt"):
    endf = np.loadtxt(path, skiprows=1)
    iaea = np.loadtxt(path.parent.parent / "iaea" / path.name, skiprows=1)
    for order in range(endf.shape[1] - 1):
        column = order + 1
        # L_l^ENDF = (A_l^IAEA / A_0^IAEA) / (2l + 1); see README.md.
        expected = iaea[:, column] / iaea[:, 1] / (2 * order + 1)
        np.testing.assert_allclose(endf[:, column], expected, rtol=tol, atol=tol)

print("All ENDF/IAEA coefficients match the expected relation.")
