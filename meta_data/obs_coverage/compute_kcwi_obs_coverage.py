"""
Script to develop how to check the observational coverage of a PHANGS target
"""

import numpy as np
import os
import pickle
from werkzeugkiste import helper_func
from obszugang import obs_info, spec_access
import matplotlib.pyplot as plt

target_list = obs_info.phangs_kcwi_galaxy_list


for target in target_list:

    # if os.path.isfile('data_output/%s_kcwi_obs_hull_dict.pickle' % target):
    #     continue

    # now get kcwi bands
    phangs_spec = spec_access.SpecAccess(spec_target_name=target)

    print(target)

    obs_hull_dict = {}

    for region_name in list(obs_info.kcwi_obs_target_dict[target].keys()):
        print(region_name)
        obs_hull_dict.update({region_name: {}})
        for grating in obs_info.kcwi_obs_target_dict[target][region_name]['gratings']:
            print(grating)

            # load kcwi cube
            phangs_spec.load_kcwi_cube(region_name=region_name, grating=grating)

            # plt.imshow(phangs_spec.kcwi_dap_map_data['dap_map_data_copt_fiducial_HA6562_FLUX'])
            # plt.show()

            spec_cube = phangs_spec.kcwi_datacube_data[region_name]['data_cube_%s' % grating]
            obs_map = np.nansum(spec_cube, axis=0)
            # get 2d WCS
            wcs = phangs_spec.kcwi_datacube_data[region_name]['wcs_2d_%s' % grating]

            # plot it
            fig = plt.figure(figsize=(20, 20))
            ax_img = fig.add_axes((0.05, 0.05, 0.94, 0.94), projection=wcs)

            ax_img.imshow(obs_map)

            # the problem here is that the pixels with the data is directly bordering to the end of the image
            # and thus a hull is hard to compute from this.
            new_obs_map = np.zeros((obs_map.shape[0] + 2, obs_map.shape[1] + 2))
            new_obs_map[1:-1, 1:-1] = obs_map

            mask_coverage = np.array(np.invert(new_obs_map == 0), dtype=float)

            hull_dict = helper_func.GeometryTools.contour2hull(data_array=mask_coverage, level=0, contour_index=0, n_max_rejection_vertice=100)
            print('n of hulls: ', len(hull_dict.keys()))

            # now save the hull points as coordinates
            hull_coord_dict = {}
            for idx in hull_dict.keys():
                ax_img.plot(hull_dict[idx]['x_convex_hull'] - 1, hull_dict[idx]['y_convex_hull'] - 1)
                # transform into coordinates
                coordinates = wcs.pixel_to_world(hull_dict[idx]['x_convex_hull'] - 1, hull_dict[idx]['y_convex_hull'] - 1)
                ra = coordinates.ra.deg
                dec = coordinates.dec.deg
                hull_coord_dict.update({idx: {'ra': ra, 'dec': dec}})

            obs_hull_dict[region_name].update({grating: hull_coord_dict})
            plt.show()

    with open('data_output/%s_kcwi_obs_hull_dict.pickle' % target,
              'wb') as file_name:
        pickle.dump(obs_hull_dict, file_name)




