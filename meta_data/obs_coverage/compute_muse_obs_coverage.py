"""
Script to develop how to check the observational coverage of a PHANGS target
"""

import numpy as np
import os
import pickle
from werkzeugkiste import helper_func
from obszugang import obs_info
from obszugang import spec_access
import matplotlib.pyplot as plt

# target_list = obs_info.phangs_muse_galaxy_list
# target_list = obs_info.phangs_muse_treasury_2_galaxy_list

target_list = ['ic1954', 'ic5273', 'ic5332', 'ngc0628', 'ngc1068', 'ngc1087', 'ngc1097', 'ngc1300', 'ngc1317', 'ngc1365', 'ngc1385', 'ngc1433', 'ngc1512', 'ngc1566', 'ngc1672', 'ngc1808', 'ngc2775', 'ngc2835', 'ngc2903', 'ngc3351', 'ngc3368', 'ngc3596', 'ngc3627', 'ngc4254', 'ngc4303', 'ngc4321', 'ngc4424', 'ngc4496a', 'ngc4535', 'ngc4548', 'ngc4579', 'ngc4689', 'ngc4694', 'ngc4731', 'ngc4941', 'ngc5068', 'ngc5248', 'ngc5643', 'ngc7496']

for target in target_list:

    # if os.path.isfile('data_output/%s_muse_obs_hull_dict.pickle' % target):
    #     continue

    # if target != 'ic5273':
    #     continue

    # if target in ['eso486_g021', 'ngc7496', 'ic1727']:
    #     continue

    # target = 'ngc2835'

    # now get muse bands
    phangs_spec = spec_access.SpecAccess(spec_target_name=target)

    print(target)

    obs_hull_dict = {}
    # for res in ['copt', 'native', '150pc', '15asec']:
    for res in ['copt']:

        # load H-alpha muse DAP
        ssp_model = 'fiducial'
        phangs_spec.load_muse_dap_map(res=res, ssp_model=ssp_model)

        print(phangs_spec.muse_dap_map_data.keys())


        data = phangs_spec.muse_dap_map_data['dap_map_data_%s_%s_HA6562_FLUX' % (res, ssp_model)]
        wcs = phangs_spec.muse_dap_map_data['dap_map_wcs_%s_%s_HA6562_FLUX' % (res, ssp_model)]

        new_nan_data = np.zeros((data.shape[0] + 2, data.shape[1] + 2)) * np.nan
        new_nan_data[1:-1, 1:-1] = data
        mask_coverage = np.array(np.invert(np.isnan(new_nan_data)), dtype=float)

        hull_dict = helper_func.GeometryTools.contour2hull(data_array=mask_coverage, level=0, contour_index=0, n_max_rejection_vertice=100)
        print(res, ' n of hulls: ', len(hull_dict.keys()))


        # fig = plt.figure(figsize=(20, 20))
        # ax_img = fig.add_axes((0.05, 0.05, 0.945, 0.945), projection=wcs)
        # ax_img.imshow(new_nan_data)
        # # plt.show()


        # now save the hull points as coordinates
        hull_coord_dict = {}
        for idx in hull_dict.keys():

            # ax_img.plot(hull_dict[idx]['x_convex_hull'], hull_dict[idx]['y_convex_hull'])

            # transform into coordinates
            coordinates = wcs.pixel_to_world(hull_dict[idx]['x_convex_hull'] - 1, hull_dict[idx]['y_convex_hull'] - 1)
            ra = coordinates.ra.deg
            dec = coordinates.dec.deg
            hull_coord_dict.update({idx: {'ra': ra, 'dec': dec}})
        obs_hull_dict.update({res: hull_coord_dict})

        # plt.show()

    if target in list(obs_info.muse_pointing_res_dict.keys()):
        for res in list(obs_info.muse_pointing_res_dict[target].keys()):
            print(res)
            # load Johnson J fake filter image

            phangs_spec.load_muse_filter_image(res=res, filter_image_band='Johnson_V')

            data = phangs_spec.muse_filter_image_data['filter_image_data_%s_Johnson_V' % res]
            wcs = phangs_spec.muse_filter_image_data['filter_image_wcs_%s_Johnson_V' % res]


            new_nan_data = np.zeros((data.shape[0] + 2, data.shape[1] + 2)) * np.nan
            new_nan_data[1:-1, 1:-1] = data
            mask_coverage = np.array(np.invert(np.isnan(new_nan_data)), dtype=float)

            hull_dict = helper_func.GeometryTools.contour2hull(data_array=mask_coverage, level=0, contour_index=0, n_max_rejection_vertice=100)
            print(res, ' n of hulls: ', len(hull_dict.keys()))

            # fig = plt.figure(figsize=(20, 20))
            # ax_img = fig.add_axes((0.05, 0.05, 0.945, 0.945), projection=wcs)
            # ax_img.imshow(new_nan_data)
            # # plt.show()

            # now save the hull points as coordinates
            hull_coord_dict = {}
            for idx in hull_dict.keys():

                # ax_img.plot(hull_dict[idx]['x_convex_hull'], hull_dict[idx]['y_convex_hull'])

                # transform into coordinates
                coordinates = wcs.pixel_to_world(hull_dict[idx]['x_convex_hull'] - 1, hull_dict[idx]['y_convex_hull'] - 1)
                ra = coordinates.ra.deg
                dec = coordinates.dec.deg
                hull_coord_dict.update({idx: {'ra': ra, 'dec': dec}})
            obs_hull_dict.update({res: hull_coord_dict})

            # plt.show()



    print(obs_hull_dict)
    print(obs_hull_dict.keys())


    # save dictionary
    if not os.path.isdir('data_output'):
        os.makedirs('data_output')

    with open('data_output/%s_muse_obs_hull_dict.pickle' % target, 'wb') as file_name:
        pickle.dump(obs_hull_dict, file_name)



