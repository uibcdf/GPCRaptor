from mdtraj import Trajectory as _mdtraj_Trajectory

def is_mdtraj_Trajectory (traj):

    return type(traj)==_mdtraj_Trajectory
