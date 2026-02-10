"""
Shared pytest fixtures and configuration for surfa tests.

This module provides common test fixtures that can be used across all test files.
"""

import pytest
import numpy as np
from pathlib import Path


# ============================================================================
# Array Fixtures
# ============================================================================

@pytest.fixture
def simple_1d_array():
    """Simple 1D array for basic testing."""
    return np.array([1, 2, 3, 4, 5])


@pytest.fixture
def simple_2d_array():
    """Simple 2D array for basic testing."""
    return np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])


@pytest.fixture
def simple_3d_array():
    """Simple 3D array for volume testing."""
    return np.ones((10, 10, 10), dtype=np.float32)


@pytest.fixture
def labeled_volume():
    """3D labeled volume with distinct regions."""
    volume = np.zeros((20, 20, 20), dtype=np.int32)
    volume[5:10, 5:10, 5:10] = 1
    volume[12:17, 12:17, 12:17] = 2
    return volume


# ============================================================================
# Geometry & Affine Fixtures
# ============================================================================

@pytest.fixture
def identity_affine():
    """4x4 identity affine transformation matrix."""
    return np.eye(4, dtype=np.float64)


@pytest.fixture
def sample_affine_matrix():
    """Sample 4x4 affine with translation and scaling."""
    affine = np.eye(4, dtype=np.float64)
    affine[0, 0] = 2.0  # Scale X
    affine[1, 1] = 2.0  # Scale Y
    affine[2, 2] = 2.0  # Scale Z
    affine[0, 3] = 10.0  # Translate X
    affine[1, 3] = 20.0  # Translate Y
    affine[2, 3] = 30.0  # Translate Z
    return affine


@pytest.fixture
def rotation_matrix_90deg():
    """Rotation matrix for 90 degrees around Z-axis."""
    rot = np.eye(4, dtype=np.float64)
    rot[0, 0] = 0.0
    rot[0, 1] = -1.0
    rot[1, 0] = 1.0
    rot[1, 1] = 0.0
    return rot


@pytest.fixture
def sample_voxel_size():
    """Standard voxel size for MRI data."""
    return np.array([1.0, 1.0, 1.0])


@pytest.fixture
def anisotropic_voxel_size():
    """Anisotropic voxel size (typical for some MRI sequences)."""
    return np.array([1.0, 1.0, 3.0])


# ============================================================================
# Mesh Fixtures
# ============================================================================

@pytest.fixture
def simple_triangle_vertices():
    """Vertices for a simple triangle."""
    return np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0]
    ], dtype=np.float32)


@pytest.fixture
def simple_triangle_faces():
    """Faces for a simple triangle."""
    return np.array([[0, 1, 2]], dtype=np.int32)


@pytest.fixture
def tetrahedron_vertices():
    """Vertices for a regular tetrahedron."""
    return np.array([
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.5, np.sqrt(3)/2, 0.0],
        [0.5, np.sqrt(3)/6, np.sqrt(6)/3]
    ], dtype=np.float32)


@pytest.fixture
def tetrahedron_faces():
    """Faces for a regular tetrahedron."""
    return np.array([
        [0, 1, 2],
        [0, 1, 3],
        [0, 2, 3],
        [1, 2, 3]
    ], dtype=np.int32)


@pytest.fixture
def unit_sphere_vertices():
    """Vertices for a simple unit sphere (ico-sphere approximation)."""
    # Simple icosahedron vertices on unit sphere
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    vertices = np.array([
        [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
        [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
        [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
    ], dtype=np.float32)
    
    # Normalize to unit sphere
    vertices = vertices / np.linalg.norm(vertices, axis=1, keepdims=True)
    return vertices


# ============================================================================
# Label & Lookup Fixtures
# ============================================================================

@pytest.fixture
def sample_label_names():
    """Sample label names for testing LabelLookup."""
    return ['background', 'white_matter', 'gray_matter', 'csf']


@pytest.fixture
def sample_label_colors():
    """Sample label colors (RGBA)."""
    return np.array([
        [0, 0, 0, 255],      # background - black
        [255, 255, 255, 255],  # white_matter - white
        [128, 128, 128, 255],  # gray_matter - gray
        [0, 0, 255, 255]       # csf - blue
    ], dtype=np.uint8)


# ============================================================================
# I/O Fixtures
# ============================================================================

@pytest.fixture
def temp_test_dir(tmp_path):
    """
    Temporary directory for I/O tests.
    
    Uses pytest's tmp_path fixture which provides a unique temporary
    directory for each test function.
    """
    return tmp_path


@pytest.fixture
def sample_nifti_filename(temp_test_dir):
    """Sample NIfTI filename in temporary directory."""
    return temp_test_dir / "test_volume.nii.gz"


@pytest.fixture
def sample_freesurfer_filename(temp_test_dir):
    """Sample FreeSurfer filename in temporary directory."""
    return temp_test_dir / "test_surface.surf"


# ============================================================================
# Slicing Fixtures
# ============================================================================

@pytest.fixture
def sample_3d_slicing():
    """Sample 3D slicing tuple."""
    return (slice(0, 10), slice(5, 15), slice(2, 8))


@pytest.fixture
def ellipsis_slicing():
    """Slicing with ellipsis."""
    return (slice(0, 5), Ellipsis, slice(2, 8))


# ============================================================================
# Orientation & Space Fixtures
# ============================================================================

@pytest.fixture
def ras_orientation():
    """RAS (Right-Anterior-Superior) orientation string."""
    return 'RAS'


@pytest.fixture
def lps_orientation():
    """LPS (Left-Posterior-Superior) orientation string."""
    return 'LPS'


@pytest.fixture
def sample_orientation_matrix():
    """Sample orientation matrix."""
    return np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ], dtype=np.float64)


# ============================================================================
# Parametrized Test Helpers
# ============================================================================

# Common dtypes for testing
COMMON_DTYPES = [np.float32, np.float64, np.int32, np.int64]

# Common shapes for testing
COMMON_SHAPES = [(10,), (10, 10), (10, 10, 10), (5, 10, 15)]

# Common ndim values
COMMON_NDIMS = [1, 2, 3, 4]


# ============================================================================
# Markers & Configuration
# ============================================================================

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests (fast, no I/O)"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests (moderate speed)"
    )
    config.addinivalue_line(
        "markers", "slow: Slow tests (I/O, large data)"
    )
    config.addinivalue_line(
        "markers", "mesh: Mesh-related tests"
    )
    config.addinivalue_line(
        "markers", "io: I/O-related tests"
    )
    config.addinivalue_line(
        "markers", "transform: Transformation tests"
    )


# ============================================================================
# Utility Functions
# ============================================================================

def assert_arrays_equal(arr1, arr2, err_msg=""):
    """Helper to assert numpy arrays are equal."""
    np.testing.assert_array_equal(arr1, arr2, err_msg=err_msg)


def assert_arrays_close(arr1, arr2, rtol=1e-7, atol=0, err_msg=""):
    """Helper to assert numpy arrays are close."""
    np.testing.assert_allclose(arr1, arr2, rtol=rtol, atol=atol, err_msg=err_msg)