from collections import namedtuple
from helper import get_pairs_matching_criteria
from json import dump

# Common combos of "is this error and/or test result" "what files to look in","search term" (eventually regex should be allowed in search term)
searchSpec = namedtuple('searchSpec',['types','files','term'])
   
NO_COMPAT = searchSpec(["er","vr"],["pipeline.exception"],"PipelineNoCompatibleSitesFoundForJob")
LAMMPS = searchSpec(["er","tr"],
                    {"CohesiveEnergyVsLatticeConstant__TD_554653289799_003":"lammps.log",
                                 "ClusterEnergyAndForces__TD_000043093022_003":"lammps_output_log/lammps.log",
                                 "TriclinicPBCEnergyAndForces__TD_892847239811_003":"lammps_output_log/lammps.log",
                                 "LinearThermalExpansionCoeffCubic__TD_522633393614_001":"screen.out"},
                                 "19 Mar 2020")  # already did pipeline.stdout for SF test, no need to re-search it
CANT_ALLOC = searchSpec(["er"],["pipeline.stderr"],"Cannot allocate memory")
CANT_ALLOC_VC = searchSpec(["vr"],["pipeline.stdout","pipeline.stderr","pipeline.exception"],"Cannot allocate memory")
# LAMMPS not built with correct package https://openkim.org/files/TE_162589006162_007-and-SM_485325656366_001-1659040207-er/pipeline.stderr
# Other memory error
# Weird MPI error
matching_pairs=get_pairs_matching_criteria(CANT_ALLOC_VC.types,CANT_ALLOC_VC.files,CANT_ALLOC_VC.term)
with open("matching_pairs_CANT_ALLOC_VC.json","w") as f:
    dump(matching_pairs,f)

