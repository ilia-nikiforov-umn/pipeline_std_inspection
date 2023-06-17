Pipeline output file inspector
==============================

This utility queries the OpenKIM repository for specified results or errors, downloads the requested pipeline.stdout or pipeline.stderr files, and looks through them for specified criteria.

Example: Find all test results between a specified date range (date range not supported yet) that have "LAMMPS 19 Mar 2020" in pipeline.stdout. Write a .json file containing a list of dicts with requested keys from each query result.

