# WarpX Data

## Overview

This repository contains data files that are too large for the main [WarpX source directory](https://github.com/ECP-WarpX/WarpX).

## Documentation

This section describes the directory structure:

Data files pertaining to a specific topic or simulation should be organized in a
folder in the repository's base directory. For example, data files containing
collision cross-sections used by the MCC and DSMC routines in WarpX are housed
in a folder named `MCC_cross_sections`. Inside that folder the cross-sections of
different atomic species are kept in separate folders.

## Contributing

Notes to follow.
At the moment, just open PRs :)

## Notes

This repository might be rebased on a regular basis to minimize size by reducing history bloat.

## License

License for warpx-data can be found at [LICENSE.txt](LICENSE.txt).
