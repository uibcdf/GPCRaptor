from .utils import is_mdtraj_Trajectory as _is_mdtraj
from numpy import zeros as _np_zeros

_helix_axis_vectors_methods = {
    'PCA' : _helix_axis_vectors_pca}

def helix_axis_vectors(traj=None, receptor=None, helix=None, method="PCA"):

    if not _is_mdtraj(traj):
        raise ValueError("Input traj needs to be an mdtraj.Trajectory class")

    if type(helix)==int:
        helix=[helix]

    vectors, geom_centers = _helix_axis_vectors_methods[method](traj,receptor,helix)

    pass

def _helix_axis_vectors(traj=None, receptor=None, helix=None):

    tmp_vectors = []
    for helix_id in helix:
        if receptor.is_coarse_grained:
            helix_heavy_atoms = traj.topology.select('name BB')
        print(helix_heavy_atoms)

    pass
