echo download ngc0253 
rclone copy drive:scratch/JWST_TECHNICAL_WORK/v4p1_beta/2987/ngc0253_2987_jwst_images.tar.gz /media/benutzer/derka_derka/data/jwst/v4p1_beta/2987 
echo unpack ngc0253 
mkdir /media/benutzer/derka_derka/data/jwst/v4p1_beta/2987/ngc0253_2987_jwst_images 
tar -xvzf /media/benutzer/derka_derka/data/jwst/v4p1_beta/2987/ngc0253_2987_jwst_images.tar.gz -C /media/benutzer/derka_derka/data/jwst/v4p1_beta/2987/ngc0253_2987_jwst_images 
rm /media/benutzer/derka_derka/data/jwst/v4p1_beta/2987/ngc0253_2987_jwst_images.tar.gz 
