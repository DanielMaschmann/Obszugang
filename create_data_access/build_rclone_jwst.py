"""
Script to create script to rclone PHANGS HST observational data from google drive
"""
import numpy as np
import os.path
from obszugang import obs_info, access_config
from werkzeugkiste import helper_func

nircam_version = 'v4p1_beta'
miri_version = 'v4p1_beta'
jwst_version = 'v4p1_beta'

program_id = 3707

target_list = list(obs_info.jwst_obs_band_dict_v4p1_beta[program_id].keys())

print(target_list)


# target_list = phangs_info.jwst_obs_band_dict.keys()

rclone_name = access_config.phangs_config_dict['rclone_name']

drive_path = 'rclone copy drive:'

jwst_rclone_file = open('download_scripts/rclone_jwst_data.sh', "w")

for target in target_list:

    path_str_jwst = ('rclone copy ' + access_config.phangs_config_dict['rclone_name'] + ':' +
                       access_config.phangs_config_dict['jwst_obs_data_drive_path_%s' % jwst_version] +
                       str(program_id) + '/')
    destination_str_jwst = (access_config.phangs_config_dict['jwst_obs_data_local_path_%s' % jwst_version] + '/' +
                              str(program_id))

    tar_file_name_on_drive = '%s_%i_jwst_images.tar.gz' % (target, program_id)


    jwst_rclone_file.writelines('echo download ' + target + ' \n')

    jwst_rclone_file.writelines(path_str_jwst + tar_file_name_on_drive + ' ' + destination_str_jwst + ' \n')

    # unpack comment
    folder_to_unpack_to = destination_str_jwst + '/' + ('%s_%i_jwst_images' % (target, program_id))
    jwst_rclone_file.writelines('echo unpack ' + target + ' \n')
    jwst_rclone_file.writelines('mkdir ' + folder_to_unpack_to + ' \n')
    jwst_rclone_file.writelines('tar -xvzf ' + destination_str_jwst + '/' + tar_file_name_on_drive +
                                ' -C ' + folder_to_unpack_to +
                                ' \n')

    # erase tar file
    jwst_rclone_file.writelines('rm ' + destination_str_jwst + '/' + tar_file_name_on_drive + ' \n')

jwst_rclone_file.close()

