from numpy import arange as _arange

receptors_info={
    'MOR' : 'Mu Opioid Receptor',
    'MOR_CG' : 'Mu Opioid Receptor in its Martini Coarse Grained version'}


receptors=list(receptors_info.keys())

class Receptor():

    name    = None
    gpcr_class = None
    gpcr_group = None
    pdbids = []


    is_coarse_grained = False

    helices = {
                1 : [],
                2 : [],
                3 : [],
                4 : [],
                5 : [],
                6 : [],
                7 : [],
                8 : []
    }


    def get_residue_indices_in_helix(self, helix=None):

        return _arange(self.helices[helix][0],self.helices[helix][1]+1)

class MOR_CG(Receptor):

    name   = 'Mu Opioid Receptor'
    gpcr_class = 'A'
    gpcr_group = 'opioid'
    pdbids = []

    is_coarse_grained = True

    helices = {
                1 : [0,31],
                2 : [37,66],
                3 : [73,106],
                4 : [116,140],
                5 : [160,197],
                6 : [204,241],
                7 : [247,275],
                8 : [277,288]
    }


