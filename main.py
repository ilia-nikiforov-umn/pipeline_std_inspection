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
LAMMPS_NOT_BUILT = searchSpec(["er","vr"],["pipeline.stdout","pipeline.stderr","pipeline.exception"],"Unrecognized pair style")
# LAMMPS not built with correct package     
# Other memory error https://openkim.org/files/TE_932922467790_000-and-SM_714124634215_000-1682711461-er/pipeline.stderr
# Weird MPI error https://openkim.org/files/VC_561022993723_004-and-SM_333792531460_001-1667944648-er/pipeline.stderr
# Too long https://openkim.org/files/TE_692192937218_004-and-MO_800536961967_002-1562949890-er/pipeline.stderr
matching_pairs=get_pairs_matching_criteria(LAMMPS_NOT_BUILT.types,LAMMPS_NOT_BUILT.files,LAMMPS_NOT_BUILT.term)
with open("matching_pairs_LAMMPS_NOT_BUILT.json","w") as f:
    dump(matching_pairs,f)

