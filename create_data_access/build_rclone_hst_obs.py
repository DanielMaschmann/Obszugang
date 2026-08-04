"""
Script to create script to rclone PHANGS HST observational data from google drive
"""
import os.path
from obszugang import obs_info, access_config
from werkzeugkiste import helper_func


if access_config.phangs_config_dict['hst_obs_target_list'] == 'all':
    target_list = list(obs_info.hst_obs_band_dict.keys())
else:
    target_list = list(access_config.phangs_config_dict['hst_obs_target_list'])

if 'm33_10.0_mpc' in target_list:
    target_list.remove('m33_10.0_mpc')
if 'ngc5194' in target_list:
    target_list.remove('ngc5194')


rclone_name = access_config.phangs_config_dict['rclone_name']

drive_path = 'rclone copy drive:'

hst_rclone_file = open('download_scripts/rclone_hst_data.sh', "w")


exception_dict_project_id = {'ngc0685': {'F657N': 'uvis657n_17457_17502'}}

for target in target_list:

    path_str = ('rclone copy ' + access_config.phangs_config_dict['rclone_name'] + ':' +
                access_config.phangs_config_dict['hst_obs_data_drive_path'] +
                helper_func.FileTools.target_names_no_zeros(target=target) + '/')

    destination_str = (access_config.phangs_config_dict['hst_obs_data_local_path'] + '/' +
                       helper_func.FileTools.target_names_no_zeros(target=target) + '/')
    check_destination_str = (access_config.phangs_config_dict['hst_obs_data_local_path'] + '/' +
                       helper_func.FileTools.target_names_no_zeros(target=target) + '/')
    # loop over bands
    for band in obs_info.hst_obs_band_dict[target]['acs']:
        print('ACS ', band)

        if target in list(exception_dict_project_id.keys()):
            if band in exception_dict_project_id[target]:
                band_folder_name = exception_dict_project_id[target][band]
            else:
                band_folder_name = 'acs' + band.lower()
        else:
            band_folder_name = 'acs' + band.lower()

        data_path = (band_folder_name + '/' + '%s_acs_%s_exp_drc_sci.fits' %
                     (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        err_path = (band_folder_name + '/' + '%s_acs_%s_err_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        wht_path = (band_folder_name + '/' + '%s_acs_%s_exp_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        if not os.path.isfile(check_destination_str + data_path):
            hst_rclone_file.writelines(path_str + data_path + ' ' + destination_str +'acs' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str + err_path):
            hst_rclone_file.writelines(path_str + err_path + ' ' + destination_str +'acs' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str + wht_path):
            hst_rclone_file.writelines(path_str + wht_path + ' ' + destination_str +'acs' + band.lower() + ' \n')

    for band in obs_info.hst_obs_band_dict[target]['uvis']:
        print('UVIS ', band)

        if target in list(exception_dict_project_id.keys()):
            if band in exception_dict_project_id[target]:
                band_folder_name = exception_dict_project_id[target][band]
            else:
                band_folder_name = 'uvis' + band.lower()
        else:
            band_folder_name = 'uvis' + band.lower()

        data_path = (band_folder_name + '/' + '%s_uvis_%s_exp_drc_sci.fits' %
                     (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        err_path = (band_folder_name + '/' + '%s_uvis_%s_err_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        wht_path = (band_folder_name + '/' + '%s_uvis_%s_exp_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), band.lower()))
        if not os.path.isfile(check_destination_str + data_path):
            hst_rclone_file.writelines(path_str + data_path + ' ' + destination_str + 'uvis' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str + err_path):
            hst_rclone_file.writelines(path_str + err_path + ' ' + destination_str + 'uvis' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str + wht_path):
            hst_rclone_file.writelines(path_str + wht_path + ' ' + destination_str + 'uvis' + band.lower() + ' \n')

    for band in obs_info.hst_obs_band_dict[target]['acs_uvis']:
        print('ACS and UVIS ', band)
        if target == 'ngc0628':
            band_folder_on_drive = band.lower() + '/'
            instrument_specification = 'acsuvis'
        elif target == 'ngc7793':
            band_folder_on_drive = 'uvis' + band.lower() + '/'
            instrument_specification = 'acs_uvis'
        else:
            raise KeyError('must be specified...')


        data_path = ('%s_%s_%s_exp_drc_sci.fits' %
                     (helper_func.FileTools.target_names_no_zeros(target=target), instrument_specification, band.lower()))
        err_path = ('%s_%s_%s_err_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), instrument_specification, band.lower()))
        wht_path = ('%s_%s_%s_exp_drc_wht.fits' %
                    (helper_func.FileTools.target_names_no_zeros(target=target), instrument_specification, band.lower()))
        if not os.path.isfile(check_destination_str +  'acs_uvis' + band.lower() + '/' + data_path):
            hst_rclone_file.writelines(path_str + band_folder_on_drive + data_path + ' ' + destination_str + 'acs_uvis' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str +  'acs_uvis' + band.lower() + '/' + err_path):
            hst_rclone_file.writelines(path_str + band_folder_on_drive + err_path + ' ' + destination_str + 'acs_uvis' + band.lower() + ' \n')
        if not os.path.isfile(check_destination_str +  'acs_uvis' + band.lower() + '/' + wht_path):
            hst_rclone_file.writelines(path_str + band_folder_on_drive + wht_path + ' ' + destination_str + 'acs_uvis' + band.lower() + ' \n')

hst_rclone_file.close()

