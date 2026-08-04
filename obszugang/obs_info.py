"""
class to gather all information need to access PHANGS (and adjacent) observational data products
"""

from numpy import unique

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# last updated: Jul 7 2025


############################################
######## all available galaxy names ########
############################################

# TO DO add missing galaxies for ALMA targets !!!!
phangs_alma_galaxy_list = [
    'ic1954', 'ic5332', 'ngc0628', 'ngc0685', 'ngc1087', 'ngc1097', 'ngc1300', 'ngc1317', 'ngc1365', 'ngc1385',
    'ngc1433', 'ngc1512', 'ngc1559', 'ngc1566', 'ngc1672', 'ngc1792', 'ngc2775', 'ngc2835', 'ngc2903',
    'ngc3351', 'ngc3621', 'ngc3627', 'ngc4254', 'ngc4298', 'ngc4303', 'ngc4321', 'ngc4535', 'ngc4536', 'ngc4548',
    'ngc4569', 'ngc4571', 'ngc4654', 'ngc4689', 'ngc4826', 'ngc5068', 'ngc5248', 'ngc6744', 'ngc7496'
]
alma_add_galaxy_list = []
full_alma_galaxy_list = phangs_alma_galaxy_list + alma_add_galaxy_list

phangs_hst_treasury_1_galaxy_list = [
    'ic1954', 'ic5332', 'ngc0628', 'ngc0628c', 'ngc0628e', 'ngc0685', 'ngc1087', 'ngc1097', 'ngc1300', 'ngc1317',
        'ngc1365', 'ngc1385', 'ngc1433', 'ngc1510', 'ngc1512', 'ngc1559', 'ngc1566', 'ngc1672', 'ngc1792', 'ngc2775',
    'ngc2835', 'ngc2903', 'ngc3351', 'ngc3621', 'ngc3627', 'ngc4254', 'ngc4298', 'ngc4303', 'ngc4321', 'ngc4535',
    'ngc4536', 'ngc4548', 'ngc4569', 'ngc4571', 'ngc4654', 'ngc4689', 'ngc4826', 'ngc5068', 'ngc5248', 'ngc6744',
    'ngc7496'
]
phangs_hst_treasury_2_galaxy_list = [
    'ic5273', 'ngc1068', 'ngc1637', 'ngc1808', 'ngc2090', 'ngc2566', 'ngc2997', 'ngc2997e', 'ngc2997w', 'ngc3059',
    'ngc3368', 'ngc3507', 'ngc3511', 'ngc3521s', 'ngc3596', 'ngc4424', 'ngc4496a', 'ngc4694', 'ngc4731', 'ngc4941',
    'ngc4951', 'ngc5042', 'ngc5530', 'ngc5643', 'ngc7456', 'ngc7793']
hst_add_galaxy_list = ['ngc5194', 'm33_10.0_mpc']
full_hst_galaxy_list = phangs_hst_treasury_1_galaxy_list + phangs_hst_treasury_2_galaxy_list + hst_add_galaxy_list

# cycle 1 proposal GO 2107
phangs_jwst_treasury_1_galaxy_list = [
    'ic5332', 'ngc0628', 'ngc1087', 'ngc1300', 'ngc1365', 'ngc1385', 'ngc1433', 'ngc1512', 'ngc1566', 'ngc1672',
    'ngc2835', 'ngc3351', 'ngc3627', 'ngc4254', 'ngc4303', 'ngc4321', 'ngc4535', 'ngc5068', 'ngc7496'
]
# cycle 2 proposal GO 3707
phangs_jwst_treasury_2_galaxy_list = [
    'ngc0685', 'ngc1068', 'ngc1097', 'ngc1317', 'ic1954', 'ngc1511', 'ngc1546', 'ngc1559', 'ngc1637', 'ngc1808',
    'ngc1809', 'ngc1792', 'ngc2090', 'ngc2283', 'ngc2566', 'ngc2775', 'ngc2903', 'ngc2997', 'ngc3059', 'ngc3137',
    'ngc3239', 'ngc3344', 'ngc3368', 'ngc3511', 'ngc3507', 'ngc3521', 'ngc3596', 'ngc3621',
    'ngc3626', 'ngc4298', 'ngc4424', 'ngc4457', 'ngc4496a', 'ngc4536', 'ngc4540', 'ngc4548', 'ngc4569', 'ngc4571',
    'ngc4579', 'ngc4654', 'ngc4689', 'ngc4694', 'ngc4694', 'ngc4731', 'ngc4781', 'ngc4826', 'ngc4941', 'ngc4951',
    'ngc5042', 'ngc5134', 'ngc5248', 'ngc5530', 'ngc5643', 'ngc6300', 'ic5273', 'ngc7456']
# cycle 3 proposal GO 4793
phangs_jwst_treasury_3_galaxy_list = [
    'ngc1097', 'ngc1433', 'ngc1512', 'ngc1637', 'ngc1672', 'ngc1792', 'ngc1808', 'ngc2903', 'ngc2997', 'ngc3351',
    'ngc3627', 'ngc4298', 'ngc4548', 'ngc5248', 'ngc5643', 'ngc6300'
]
jwst_add_galaxy_list = ['ngc5194']
full_jwst_galaxy_list = list(unique(phangs_jwst_treasury_1_galaxy_list + phangs_jwst_treasury_2_galaxy_list +
                                    phangs_jwst_treasury_3_galaxy_list + jwst_add_galaxy_list))

# see Hassani+2024 2024ApJS..271....2H
astrosat_galaxy_list = [
    'ic5332', 'ngc0253', 'ngc0300', 'ngc0628', 'ngc1097', 'ngc1300', 'ngc1317', 'ngc1365', 'ngc1385', 'ngc1433',
    'ngc1512', 'ngc1546', 'ngc1566', 'ngc2090', 'ngc2835', 'ngc2903', 'ngc3351', 'ngc3621', 'ngc3627', 'ngc4254',
    'ngc4298', 'ngc4321', 'ngc4476', 'ngc4535', 'ngc4571', 'ngc4579', 'ngc4654', 'ngc5128', 'ngc6744', 'ngc7496',
    'ngc7793']
astrosat_add_galaxy_list = []
full_astrosat_galaxy_list = astrosat_galaxy_list + astrosat_add_galaxy_list

# TO DO add missing galaxies !!!!
phangs_muse_treasury_1_galaxy_list = [
    'ic5332', 'ngc0628', 'ngc1087', 'ngc1300', 'ngc1365', 'ngc1385', 'ngc1433', 'ngc1512', 'ngc1566', 'ngc1672',
    'ngc2835', 'ngc3351', 'ngc3627', 'ngc4254', 'ngc4303', 'ngc4321', 'ngc4535', 'ngc5068', 'ngc7496']

phangs_muse_treasury_2_galaxy_list = ['eso486_g021', 'ic1727', 'ic1954', 'ic5273', 'ngc0524', 'ngc1068', 'ngc1097',
                                      'ngc1317', 'ngc1510', 'ngc1808', 'ngc2775', 'ngc2903', 'ngc3239', 'ngc3274',
                                      'ngc3368', 'ngc3489', 'ngc3521', 'ngc3596', 'ngc3599', 'ngc3607', 'ngc3626',
                                      'ngc4424', 'ngc4435', 'ngc4457', 'ngc4496a', 'ngc4548', 'ngc4579', 'ngc4596',
                                      'ngc4689', 'ngc4694', 'ngc4697', 'ngc4731', 'ngc4781', 'ngc4941', 'ngc5248',
                                      'ngc5643', 'ngc7456', 'ngc7743', 'ugc685', 'ugc5340']

phangs_muse_galaxy_list = phangs_muse_treasury_1_galaxy_list + phangs_muse_treasury_2_galaxy_list

# phangs_muse_jwst_cycle_2_overlap_galaxy_list = ['ic5273', 'ngc1068', 'ngc1097', 'ngc1317', 'ngc1808', 'ngc2775',
#                                                 'ngc2903', 'ngc3368', 'ngc3521', 'ngc4424', 'ngc4457', 'ngc4548',
#                                                 'ngc4694', 'ngc4941', 'ngc5248',]
#
# phangs_muse_etg_galaxy_list = ['ngc0524', 'ngc1317', 'ngc3489', 'ngc3599', 'ngc3607', 'ngc3626', 'ngc4435', 'ngc4457',
#                                'ngc4596', 'ngc4694', 'ngc4697', 'ngc7743',]
#
# phangs_muse_alma_dwarf_galaxy_list = ['ic1954', 'ngc3239', 'ngc3596', 'ngc4496a', 'ngc4731', 'ngc4781', 'ngc7456']
#
# phangs_muse_d_sub_5mpc_galaxy_list = ['eso097-013' , 'ngc4945', 'ngc5236']
#
# phangs_muse_galaxy_list = (phangs_muse_jwst_cycle_2_overlap_galaxy_list +
#                            phangs_muse_etg_galaxy_list + phangs_muse_alma_dwarf_galaxy_list +
#                            phangs_muse_d_sub_5mpc_galaxy_list)

# TO DO add missing galaxies !!!!
phangs_kcwi_galaxy_list = [
    'ngc0628', 'ngc1087', 'ngc1300', 'ngc1385', 'ngc2835', 'ngc3627', 'ngc3239', 'ngc5068', 'ngc5194'
]

phangs_chandra_galaxy_list = [
    'ic5332', 'ngc0628', 'ngc1087', 'ngc1300', 'ngc1365', 'ngc1433', 'ngc1512',  'ngc1566', 'ngc1672',
    'ngc2835', 'ngc3351', 'ngc3627', 'ngc4254', 'ngc4303', 'ngc4321', 'ngc4535', 'ngc5068', 'ngc5194'
]



#################################################################
##### specific observation available for individual targets #####
#################################################################
#
# which versions are available?
nircam_available_data_versions = ['v0p2', 'v1p1p1', 'v2p0', 'v0p3p2', 'v4p1_beta']
miri_available_data_versions = ['v0p3', 'v1p1p1', 'v2p0', 'v0p3p2', 'v4p1_beta']
astrosat_available_data_versions = ['v1p0']
# note that HST does not have a version number as it is a rolling release

hst_obs_band_dict = {
    'm33_10.0_mpc': {
        'acs': ['F475W', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},

    'ic1954':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ic5273':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W',  'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ic5332':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc0628':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': ['F555W', 'F658N'],
         'ir': []},
    'ngc0628c':
        {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},
    'ngc0628e':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W', 'F658N'],
         'acs_uvis': [],
         'ir': []},
    'ngc0685':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1068':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1087':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1097':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1300':
        {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1317':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1365':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1385':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1433':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1511':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1512':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1546':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1559':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F606W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1566':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1637':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1672':
        {'acs': ['F435W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1792':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1808':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1809':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2090':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2566':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2775':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2835':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2903':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2997':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2997e':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2997w':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3059':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3137':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3351':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F547M', 'F555W', 'F657N', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3368':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3507':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3511':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3521s':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3596':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3621':
        {'acs': ['F435W', 'F555W', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F657N'],
         'acs_uvis': [],
         'ir': []},
    'ngc3627':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4254':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4298':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4303':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4321':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4424':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4496a':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4535':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4536':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4548':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4569':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4571':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4579':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4654':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4689':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4694':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4731':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4826':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4941':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4951':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5042':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5068':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5194':
        {'acs': ['F435W', 'F555W', 'F814W', 'F658N'],
         'uvis': ['F275W', 'F336W', 'F689M'],
         'acs_uvis': [],
         'ir': [
             #'F110W', 'F128N'
                ]},
    'ngc5248':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5530':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5643':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc6300':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc6744':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F547M', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc7456':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc7496':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc7793':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F657N'],
         'acs_uvis': ['F555W', 'F814W'],
         'ir': []},
        }


jwst_obs_band_dict_v1p1p1 = {
    'ic5332': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
               'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc0628': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1087': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1300': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1365': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1385': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1433': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1512': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1566': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1672': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc2835': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc3351': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc3627': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4254': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4303': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4321': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4535': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc5068': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc7496': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
}

jwst_obs_band_dict_v2p0 = {
    'ic1954': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
               'miri_observed_bands': ['F770W', 'F2100W']},
    'ic5273': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
               'miri_observed_bands': ['F770W', 'F2100W']},
    'ic5332': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
               'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc0628': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc0685': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
               'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1068': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
               'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1087': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1097': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1300': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1317': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1365': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1385': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1433': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1511': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1512': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1546': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1559': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1566': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1637': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1672': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc1792': {'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', 'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1808': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc1809': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2090': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2283': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2566': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2775': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2835': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc2903': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc2997': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3059': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3137': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3239': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3344': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3351': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc3368': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3507': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3511': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3521': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3596': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3621': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3626': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc3627': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4254': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4298': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4303': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4321': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4424': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4457': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4496a': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                 'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4535': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4536': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4540': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4548': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4569': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4571': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4579': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4654': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4689': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4694': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4731': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4781': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4826': {'nircam_observed_bands': ['F150W', 'F187N', 'F200W', 'F300M', 'F335M', 'F405N', 'F430M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc4941': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc4951': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc5042': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc5068': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
    'ngc5134': {'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc5248': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc5643': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc6300': {'nircam_observed_bands': ['F150W', 'F164N',  'F187N', 'F200W', 'F212N',  'F277W',  'F300M', 'F335M', 'F360M', 'F405N', 'F444W'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc7456': {'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
                'miri_observed_bands': ['F770W', 'F2100W']},
    'ngc7496': {'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
                'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
}

# this is the data available from the M51 data release
jwst_obs_band_dict_v0p2 = {
    'ngc5194': {'nircam_observed_bands': [],
                'miri_observed_bands': ['F560W', 'F770W', 'F1000W', 'F1130W', 'F1280W', 'F1500W', 'F1800W', 'F2100W']}
}

jwst_obs_band_dict_v0p3 = {
        'ngc5194': {'nircam_observed_bands': ['F115W', 'F140M', 'F150W', 'F164N', 'F182M', 'F187N', 'F200W', 'F210M',
                                              'F212N', 'F250M', 'F300M', 'F335M', 'F360M', 'F405N', 'F430M', 'F444W'],
                    'miri_observed_bands': []}
}

jwst_obs_band_dict_v0p3p2 = {
        'ngc5194': {'nircam_observed_bands': ['F115W', 'F140M', 'F150W', 'F164N', 'F182M', 'F187N', 'F200W', 'F210M',
                                              'F212N', 'F250M', 'F300M', 'F335M', 'F360M', 'F405N', 'F430M', 'F444W'],
                    'miri_observed_bands': ['F560W', 'F770W', 'F1000W', 'F1130W', 'F1280W', 'F1500W', 'F1800W',
                                            'F2100W']}
}


jwst_obs_band_dict_v4p1_beta = {
    2107: {
        'ic5332': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc0628': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1087': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1300': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1365': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1385': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1433': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1512': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1566': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc1672': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc2835': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc3351': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc3627': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc4254': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc4303': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc4321': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc4535': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc5068': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']},
        'ngc7496': {
            'nircam_observed_bands': ['F200W', 'F300M', 'F335M', 'F360M'],
            'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W']}
    },

    2987: {
        'ngc0253': {
            'nircam_observed_bands': [],
            'miri_observed_bands': []}
    },

    3177: {
        'ngc4826': {
            'nircam_observed_bands': [],
            'miri_observed_bands': []}
    },

    3707: {
        'ic1954': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ic5273': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc0685': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1068': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1097': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1317': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1511': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1546': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1559': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1637': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1792': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1808': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc1809': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2090': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2283': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2566': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2775': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2903': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc2997': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3059': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3137': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3239': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3344': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3368': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3507': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3511': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3521': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3596': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3621': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc3626': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4298': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4424': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4457': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4496a': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4536': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4540': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4548': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4569': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4571': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4579': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4654': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4689': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4694': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4731': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4781': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4826': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4941': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc4951': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc5042': {
            'nircam_observed_bands': ['F150W', 'F187N', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']},
        'ngc5134': {
            'nircam_observed_bands': ['F150W', 'F200W', 'F300M', 'F335M'],
            'miri_observed_bands': ['F770W',  'F2100W']}
    },

    4793: {
        'ngc1097': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1433': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1512': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1637': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1672': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1792': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc1808': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc2903': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc2997': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc3351': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc3627': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc4298': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc4548': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc5248': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc5643': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
        'ngc6300': {
            'nircam_observed_bands': ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W',  'F335M', 'F360M', 'F405N',
                                       'F444W'],
            'miri_observed_bands': []},
    },

    7978: {
        'ngc0628': {
            'nircam_observed_bands': [],
            'miri_observed_bands': []},
    },
}


jwst_obs_band_dict_v4p1_beta_old = {
    'ngc1672': {
        'nircam_observed_bands':
            ['F200W', 'F300M', 'F335M', 'F360M', 'F150W', 'F164N', 'F187N', 'F212N', 'F277W', 'F405N', 'F444W'],
        'nircam_program_id':
            {
                'F200W': 2107,
                'F300M': 2107,
                'F335M': 2107,
                'F360M': 2107,
                'F150W': 4793,
                'F164N': 4793,
                'F187N': 4793,
                'F212N': 4793,
                'F277W': 4793,
                'F405N': 4793,
                'F444W': 4793

            },
        'miri_observed_bands': ['F770W', 'F1000W', 'F1130W', 'F2100W'],
        'miri_program_id':
            {
                'F770W': 2107,
                'F1000W': 2107,
                'F1130W': 2107,
                'F2100W': 2107
            },
    },

    'ngc1097': {
        'nircam_observed_bands':
            ['F150W', 'F164N', 'F187N', 'F200W', 'F212N', 'F277W', #'F300M',
             'F335M', 'F360M', 'F405N', 'F444W'],
        'nircam_program_id':
            {
                'F150W': 4793,
                'F164N': 4793,
                'F187N': 4793,
                'F200W': 4793,
                'F212N': 4793,
                'F277W': 4793,
                'F335M': 4793,
                'F360M': 4793,
                'F405N': 4793,
                'F444W': 4793

            },
        'miri_observed_bands': ['F770W', 'F2100W'],
        'miri_program_id':
            {
                'F770W': 3707,
                'F2100W': 3707
            },
    },


}





# see Hassani+2024 2024ApJS..271....2H
astrosat_obs_band_dict_v1p0 = {
    'ic5332': {'observed_bands': ['F148W']},
    'ngc0253': {'observed_bands': ['F169M', 'N219M', 'N263M']},
    'ngc0300': {'observed_bands': ['F148W', 'F154W', 'F169M', 'F172M', 'N219M', 'N245M', 'N263M']},
    'ngc0628': {'observed_bands': ['F148W', 'F154W', 'F169M', 'F172M', 'N242W', 'N219M', 'N245M', 'N263M', 'N279N']},
    'ngc1097': {'observed_bands': ['F148W']},
    'ngc1300': {'observed_bands': ['F148W']},
    'ngc1317': {'observed_bands': ['F148W', 'F154W', 'F169M', 'F172M', 'N219M']},
    'ngc1365': {'observed_bands': ['F148W', 'F169M', 'F172M', 'N219M', 'N263M', 'N279N']},
    'ngc1385': {'observed_bands': ['F148W']},
    'ngc1433': {'observed_bands': ['F154W', 'F169M', 'N219M', 'N245M', 'N263M', 'N279N']},
    'ngc1512': {'observed_bands': ['F154W', 'N242W', 'N245M', 'N263M']},
    'ngc1546': {'observed_bands': ['F148W']},
    'ngc1566': {'observed_bands': ['F148W', 'F154W', 'F172M', 'N219M', 'N263M']},
    'ngc2090': {'observed_bands': ['F148W']},
    'ngc2835': {'observed_bands': ['F148W']},
    'ngc2903': {'observed_bands': ['F148W', 'F169M', 'N219M', 'N263M']},
    'ngc3351': {'observed_bands': ['F148W']},
    'ngc3621': {'observed_bands': ['F148W', 'F172M']},
    'ngc3627': {'observed_bands': ['F148W']},
    'ngc4254': {'observed_bands': ['F154W']},
    'ngc4298': {'observed_bands': ['F148W']},
    'ngc4321': {'observed_bands': ['F154W']},
    'ngc4476': {'observed_bands': ['F154W', 'N242W']},
    'ngc4535': {'observed_bands': ['F148W']},
    'ngc4571': {'observed_bands': ['F154W', 'N263M']},
    'ngc4579': {'observed_bands': ['F154W']},
    'ngc4654': {'observed_bands': ['F148W']},
    'ngc5128': {'observed_bands': ['F148W', 'N219M', 'N245M', 'N279N']},
    'ngc6744': {'observed_bands': ['F148W']},
    'ngc7496': {'observed_bands': ['F148W']},
    'ngc7793': {'observed_bands': ['F148W', 'N242W']}
}

# for MUSE the needed information is the resolution for the made observations
muse_obs_res_dict = {
    # treasury 1
    'ic5332': {'copt_res': 0.87},
    'ngc0628': {'copt_res': 0.92},
    'ngc1087': {'copt_res': 0.92},
    'ngc1300': {'copt_res': 0.89},
    'ngc1365': {'copt_res': 1.15},
    'ngc1385': {'copt_res': 0.77},
    'ngc1433': {'copt_res': 0.91},
    'ngc1512': {'copt_res': 1.25},
    'ngc1566': {'copt_res': 0.80},
    'ngc1672': {'copt_res': 0.96},
    'ngc2835': {'copt_res': 1.15},
    'ngc3351': {'copt_res': 1.05},
    'ngc3627': {'copt_res': 1.05},
    'ngc4254': {'copt_res': 0.89},
    'ngc4303': {'copt_res': 0.78},
    'ngc4321': {'copt_res': 1.16},
    'ngc4535': {'copt_res': 0.56},
    'ngc5068': {'copt_res': 1.04},
    'ngc7496': {'copt_res': 0.89},


    # treasury 2 and additional galaxies
    'eso486_g021': {'copt_res': 1.09},
    'ic1727': {'copt_res': 0.93},
    'ic1954': {'copt_res': 0.80},
    'ic5273': {'copt_res': 0.55},
    'ngc0524': {'copt_res': 0.70},
    'ngc1068': {'copt_res': 0.66},
    'ngc1097': {'copt_res': 0.70},
    'ngc1317': {'copt_res': 0.89},
    'ngc1510': {'copt_res': 1.10},
    'ngc1808': {'copt_res': 0.76},
    'ngc2775': {'copt_res': 0.50},
    'ngc2903': {'copt_res': 1.24},
    'ngc3239': {'copt_res': 0.66},
    'ngc3274': {'copt_res': 0.76},
    'ngc3368': {'copt_res': 0.41},
    'ngc3489': {'copt_res': 0.83},
    'ngc3521': {'copt_res': 0.40},
    'ngc3596': {'copt_res': 1.05},
    'ngc3599': {'copt_res': 0.82},
    'ngc3607': {'copt_res': 0.85},
    'ngc3626': {'copt_res': 0.37},
    'ngc4424': {'copt_res': 1.04},
    'ngc4435': {'copt_res': 0.67},
    'ngc4457': {'copt_res': 0.36},
    'ngc4496a': {'copt_res': 0.89},
    'ngc4548': {'copt_res': 0.50},
    'ngc4579': {'copt_res': 1.04},
    'ngc4596': {'copt_res': 0.57},
    'ngc4689': {'copt_res': 0.66},
    'ngc4694': {'copt_res': 0.75},
    'ngc4697': {'copt_res': 0.62},
    'ngc4731': {'copt_res': 1.21},
    'ngc4781': {'copt_res': 0.93},
    'ngc4941': {'copt_res': 0.78},
    'ngc5248': {'copt_res': 0.61},
    'ngc5643': {'copt_res': 0.49},
    'ngc7456': {'copt_res': 0.74},
    'ngc7743': {'copt_res': 0.98},
    'ugc685': {'copt_res': 0.76},
    'ugc5340': {'copt_res': 1.37}


}

muse_pointing_res_dict = {
    'ngc1365':
        {
            'P01': 0.708,
            'P02': 0.821,
            'P03': 0.831,
            'P04': 0.899,
            'P05': 0.923,
            'P06': 0.716,
            'P07': 0.640,
            'P08': 0.902,
            'P09': 0.901,
            'P10': 1.081,
            'P11': 0.583,
            'P12': 0.756,
            'P30': 0.823,
        }
}


# taken from Rickards Vaught et al. 2024 (2024ApJ...966..130R)
kcwi_obs_res_fwhm_dict = {
    'ngc0628': {
        'combined': {
            'bl_large': 2.0,
            'bl_large_err': 0.4,
        }
    },
    'ngc1087': {
        'combined': {
            'bl_large': 1.2,
            'bl_large_err': 0.1
        }
    },
    'ngc1300': {
        'combined': {
            'bl_large': 1.3,
            'bl_large_err': 0.1
        }
    },
    'ngc1385': {
        'combined': {
            'bl_large': 1.3,
            'bl_large_err': 0.1
        }
    },
    'ngc2835': {
        'combined': {
            'bl_large': 1.4,
            'bl_large_err': 0.1
        }
    },
    'ngc3239': {
        'combined': {
            'bl_large': 0.1,
            'bl_large_err': 0.1
        }
    },
    'ngc3627': {
        'combined': {
            'bl_large': 1.1,
            'bl_large_err': 0.1
        }
    },
    'ngc5068': {
        'combined': {
            'bl_large': 1.5,
            'bl_large_err': 0.4
        }
    },
}

# Keck KCWI observations
kcwi_obs_target_dict = {

    'ngc0628': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc1087': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc1300': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc1385': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc2835': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },

    'ngc3239': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc3627': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc5068': {
        'combined': {
            'file_id': None,
            'gratings': ['bl_large'],
        }
    },
    'ngc5194': {
        'NE': {
            'file_id': 'ne',
            'gratings': ['bl_small', 'bh3_small', 'rh1_small', 'rl7150_small', 'rl8950_small'],
        },
        'E': {
            'file_id': 'e',
            'gratings': ['bl_small', 'bh3_small', 'rh1_small', 'rl7150_small', 'rl8950_small'],
        },
        'SW': {
            'file_id': 'sw',
            'gratings': ['bl_small', 'bh3_small', 'rh1_small', 'rl7150_small', 'rl8950_small'],
        },
    },
}


# new galaxies observed with KCWI
# see https://drive.google.com/drive/folders/1KGLBR7rJcC_8tfte75f-gHh_iqjAjS13
# gratings: bl_large and rl7150_small



# JWST spectroscopy
nirspec_obs_target_dict = {
    'ngc5194': {
        'NE': {
            'karin_reduction_v1_oct2024': {
                'file_id': 'jw03435-o004_t005',
                'gratings': ['G140M/F100LP', 'G235M/F170LP', 'G395M/F290LP']}
        },
        'E': {
            'karin_reduction_v1_oct2024': {
                'file_id': 'jw03435-o006_t010',
                'gratings': ['G140M/F100LP', 'G235M/F170LP', 'G395M/F290LP']}
        },
        'SW': {
            'karin_reduction_v1_oct2024': {
                'file_id': 'jw03435-o012_t014',
                'gratings': ['G140M/F100LP', 'G235M/F170LP', 'G395M/F290LP']}
        },
    },
}

miri_mrs_obs_target_dict = {
    'ngc5194': {
        'NE': {
            'karin_reduction': {
                'file_id': 'Arm1',
                'channels': ['CH1', 'CH2', 'CH3', 'CH4']}
        },
        'E': {
            'karin_reduction': {
                'file_id': 'Arm3',
                'channels': ['CH1', 'CH2', 'CH3', 'CH4']}
        },
        'SW': {
            'karin_reduction': {
                'file_id': 'Arm2',
                'channels': ['CH1', 'CH2', 'CH3', 'CH4']}
        },
    },
}




###########################################
######## Value added data products ########
###########################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!! TO DO: make cluster catalog list version depending !!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
hst_cluster_cat_target_list = ['ic1954', 'ic5332', 'ngc0628e', 'ngc0628c', 'ngc0685', 'ngc1087', 'ngc1097',
                               'ngc1300', 'ngc1317', 'ngc1365', 'ngc1385', 'ngc1433', 'ngc1510', 'ngc1512',
                               'ngc1559', 'ngc1566', 'ngc1672', 'ngc1792', 'ngc2775', 'ngc2835', 'ngc2903',
                               'ngc3351', 'ngc3621', 'ngc3627', 'ngc4254', 'ngc4298', 'ngc4303', 'ngc4321',
                               'ngc4535', 'ngc4536', 'ngc4548', 'ngc4569', 'ngc4571', 'ngc4654', 'ngc4689',
                               'ngc4826', 'ngc5068', 'ngc5248', 'ngc6744', 'ngc7496']

hst_cluster_cat_hst_ha_target_list = [
    'ic5332', 'ngc0628e', 'ngc0628c', 'ngc1087', 'ngc1097', 'ngc1300', 'ngc1365', 'ngc1385',
                                      'ngc1433', 'ngc1512', 'ngc1566', 'ngc1672', 'ngc3351', 'ngc3627', 'ngc4254',
                                      'ngc4303', 'ngc4321', 'ngc5068', 'ngc7496']

hst_ha_cont_sub_dict = {
    'ic5332': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc0628c': {'uvis': None, 'acs': 'F658N', 'cont_sub': True},
    'ngc0628e': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc1087': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc1097': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc1300': {'uvis': None, 'acs': 'F658N', 'cont_sub': True},
    'ngc1365': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc1385': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc1433': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc1512': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc1566': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc1672': {'uvis': None, 'acs': 'F658N', 'cont_sub': True},
    'ngc2775': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc2835': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc3059': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc3351': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc3627': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    # 'ngc4254e': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    # 'ngc4254w': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4254': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4303': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc4321': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4536': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4596': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4571': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4689': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4731': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4826': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc4951': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    # 'ngc5068n': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    # 'ngc5068s': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc5068': {'uvis': 'F658N', 'acs': None, 'cont_sub': True},
    'ngc5194': {'uvis': None, 'acs': 'F658N', 'cont_sub': True},
    'ngc5236': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc6744': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
    'ngc7496': {'uvis': 'F657N', 'acs': None, 'cont_sub': True},
}

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!! TO DO: make cluster catalog list version depending !!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
hst_cluster_cat_obs_band_dict = {
    'ic1954':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ic5332':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc0628e':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W']},
    'ngc0628c':
        {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W']},
    'ngc0685':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1087':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1097':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1300':
        {'acs': ['F435W', 'F555W', 'F814W'],
         'uvis': ['F275W', 'F336W']},
    'ngc1317':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1365':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1385':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1433':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1510':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1512':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1559':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1566':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc1672':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W']},
    'ngc1792':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc2775':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc2835':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc2903':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc3351':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc3621':
        {'acs': ['F435W', 'F555W', 'F814W'],
         'uvis': ['F275W', 'F336W']},
    'ngc3627':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4254':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4298':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4303':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4321':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4535':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4536':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4548':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4569':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4571':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4654':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4689':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc4826':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc5068':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc5248':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc6744':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
    'ngc7496':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W']},
        }

############################
##### PSF availability #####
############################
acs_wfc_psf_band_list = ['F435W', 'F475W', 'F606W', 'F625W', 'F658N', 'F775W', 'F814W', 'F850L']
wfc3_uv_psf_band_list = ['F225W', 'F275W', 'F336W', 'F390W', 'F438W', 'F467M', 'F555W', 'F606W', 'F621M', 'F775W',
                         'F814W', 'F850L']
wfc3_ir_psf_band_list = ['F098M', 'F105W', 'F110W', 'F125W', 'F127M', 'F140W', 'F153M', 'F160W']


######################
###### OLD CODE ######
######################

hst_obs_band_dict_old = {
    'ic1954':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ic5332':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc0628':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': ['F555W', 'F658N'],
         'ir': []},
    'ngc0628c':
        {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},
    'ngc0628e':
        {'acs': ['F435W', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W', 'F658N'],
         'acs_uvis': [],
         'ir': []},
    'ngc0685':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1087':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1097':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1300':
        {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1317':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1365':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1385':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1433':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1512':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1510':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1559':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1566':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1672':
        {'acs': ['F435W', 'F658N', 'F814W'],
         'uvis': ['F275W', 'F336W', 'F555W'],
         'acs_uvis': [],
         'ir': []},
    'ngc1792':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2775':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2835':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2903':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc2997e':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3059':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3351':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3368':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3621':
        {'acs': ['F435W', 'F555W', 'F814W'],
         'uvis': ['F275W', 'F336W'],
         'acs_uvis': [],
         'ir': []},
    'ngc3627':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4254':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4298':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4303':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4321':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4424':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4535':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W',
                  'F657N',
                  'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4536':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4548':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4569':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4571':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4654':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4689':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4694':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4731':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4826':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc4951':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc5068':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F658N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    # 'ngc5194':
    #     {'acs': ['F435W', 'F555W', 'F658N', 'F814W'],
    #      'uvis': ['F275W', 'F336W'],
    #      'acs_uvis': [],
    #      'ir}: [,
    'ngc5248':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc6744':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc7496':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W', 'F555W', 'F657N', 'F814W'],
         'acs_uvis': [],
         'ir': []},
    'ngc7793':
        {'acs': [],
         'uvis': ['F275W', 'F336W', 'F438W'],
         'acs_uvis': ['F555W', 'F814W'],
         'ir': []},
        }
