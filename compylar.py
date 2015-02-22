#/usr/bin/python2.7

import argparse
import os

__author__ = "Axel Diaz"
__credits__ = ["Axel Diaz"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Axel Diaz"
__email__ = "diaz.axelio@gmail.com"
__status__ = "Development"


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--ubicacion', dest='ubicacion',
                        action='store_true',
                        help='Directorio donde estan ubicados los drivers')
    parser.add_argument('-w', '--wl_apsta', dest='wl_apsta',
                        action='store_true', default='3.130.20.0.o',
                        help='Version del wl_apsta. (Por defecto: 3.130.20.0.o)')
    parser.add_argument('-b', '--b43', dest='b43',
                        action='store_true', default='4.150.10.5',
                        help='Version del b43-fwcutter. (Por defecto: 4.150.10.5)')

    args = parser.parse_args()

    comandos = []
    comandos.append('b43-fwcutter -w /lib/firmware\
                     %swl_apsta-3.130.20.0.o' % (args.ubicacion, args.wl_apsta))

    comandos.append('b43-fwcutter --unsupported -w /lib/firmware\
                    %sbroadcom-wl-%s/driver/wl_apsta_mimo.o' % (
                        args.ubicacion, args.b43))
    comandos.append('b43-fwcutter --unsupported -w /lib/firmware\
                    %sbroadcom-wl-%s/driver/wl_apsta_mimo.o' % (
                        args.ubicacion, args.b43))
    comandos.append('apt-key adv --recv-keys --keyserver\
                     pgp.mit.edu 8C720439')

    cmd = ''
    for comando in comandos:
        cmd = '%s ; %s' % (cmd, comando)

    os.system('su -c %s' % (cmd))


__main__()
