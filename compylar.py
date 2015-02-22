#!/usr/bin/python2.7

import argparse
import os

from VERSION import version


def extant_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        raise argparse.ArgumentError("{0} does not exist".format(x))
    return x


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version',                    
                        version="%s" % (version))
    parser.add_argument('-u', '--ubicacion', dest='ubicacion',
                        required=True,
                        help='Directorio donde estan ubicados los drivers',
                        type=extant_file, metavar="ARCHIVO")
    parser.add_argument('-w', '--wl_apsta', dest='wl_apsta',
                        action='store_true', default='3.130.20.0.o',
                        help='Version del wl_apsta. (Por defecto: 3.130.20.0.o)')
    parser.add_argument('-b', '--b43', dest='b43',
                        action='store_true', default='4.150.10.5',
                        help='Version del b43-fwcutter. (Por defecto: 4.150.10.5)')

    args = parser.parse_args()

    archivo_deb = 'b43-fwcutter_011-1_i386.deb'
    compilar_deb = 'dpkg -i %s%s' % (args.ubicacion, archivo_deb)
    agregar_driver = 'b43-fwcutter -w /lib/firmware\
                      %swl_apsta-%s' % (
                        args.ubicacion, args.wl_apsta)
    agregar_driver = '%s; b43-fwcutter --unsupported -w /lib/firmware\
                    %sbroadcom-wl-%s/driver/wl_apsta_mimo.o' % (
                        agregar_driver, args.ubicacion, args.b43)
    agregar_llave = 'apt-key adv --recv-keys --keyserver\
                     pgp.mit.edu 8C720439'

    os.system('su -c "%s; %s; %s"' % (compilar_deb,
        agregar_driver, agregar_llave))


__main__()
