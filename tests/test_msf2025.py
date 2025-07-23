import pytest
import numpy as np

def test_calculate_angle():
    from msf2025.measure import calculate_angle
    rA = np.array([0, 0, -1])
    rB = np.array([0, 0, 0])
    rC = np.array([1, 0, 0])
    expected_angle_degrees = 90
    expected_angle_radians = expected_angle_degrees / 180 * np.pi
    calculated_angle_degrees = calculate_angle(rA, rB, rC, degrees=True)
    calculated_angle_radians = calculate_angle(rA, rB, rC, degrees=False)
    assert np.allclose(expected_angle_degrees, calculated_angle_degrees, atol=1e-6)
    assert np.allclose(expected_angle_radians, calculated_angle_radians, atol=1e-6)


def test_build_bond_list():
    from msf2025.molecule import build_bond_list
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])
    expected_bonds = {(0, 1), (0, 2), (0, 3), (0, 4)}
    calculated_bonds = build_bond_list(coordinates)
    assert expected_bonds == set(calculated_bonds.keys())
    for bond_length in calculated_bonds.values():
        assert np.allclose(bond_length, 1.4, atol=1e-6)

    with pytest.raises(ValueError):
        build_bond_list(coordinates, min_bond=-1)

# @pytest.fixture
# def methane_molecule():
#     atom_types = ['C', 'H', 'H', 'H', 'H']
#     coordinates = np.array([
#         [1, 1, 1],
#         [2.4, 1, 1],
#         [-0.4, 1, 1],
#         [1, 1, 2.4],
#         [1, 1, -0.4]
#     ])
#     return atom_types, coordinates


# @pytest.mark.parametrize("max_bond", np.linspace(1, 5, 4))
# @pytest.mark.parametrize("min_bond", np.linspace(0, 0.5, 4))
# def test_build_bond_list_again(methane_molecule, max_bond, min_bond):
#     coordinates = methane_molecule[1]