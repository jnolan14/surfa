# _____
# SURFA
#

__version__ = '0.6.0'

from . import system as system

from .core import stack as stack
from .core import labels as labels
from .core import slicing as slicing
from .core import LabelLookup as LabelLookup
from .core import LabelRecoder as LabelRecoder

from .transform import Affine as Affine
from .transform import Warp as Warp
from .transform import Space as Space
from .transform import ImageGeometry as ImageGeometry

from .image import Volume as Volume
from .image import Slice as Slice

from .mesh import Mesh as Mesh
from .mesh import Overlay as Overlay
from .mesh import sphere as sphere

from .io import load_volume as load_volume
from .io import load_slice as load_slice
from .io import load_overlay as load_overlay
from .io import load_affine as load_affine
from .io import load_label_lookup as load_label_lookup
from .io import load_mesh as load_mesh
from .io import load_warp as load_warp

from . import vis as vis
from . import freesurfer as freesurfer
from . import pipeline as pipeline
