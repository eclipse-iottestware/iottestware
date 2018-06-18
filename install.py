###############################################################################
# Copyright (c) 2018  Fraunhofer FOKUS                                        #
# All rights reserved. This program and the accompanying materials            #
# are made available under the terms of the Eclipse Public License v1.0       #
# which accompanies this distribution, and is available at                    #
# http://www.eclipse.org/legal/epl-v10.html                                   #
#                                                                             #
# Contributors:                                                               #
#       Sascha Hackel                                                         #
#       Alexander Kaiser                                                      #
###############################################################################

""""""""""""""""""
"""  IMPORTS   """
""""""""""""""""""
import os
from os.path import expanduser
import subprocess
import argparse
import glob

""""""""""""""""""""""""
"""  CONFIGURATION   """
""""""""""""""""""""""""

# home directory
HOME = expanduser("~")


parser = argparse.ArgumentParser(description='Installing and running the IoT-Testware. Please specify a mode.')
parser.add_argument("-p", "--protocol", required=True, choices=['mqtt', 'coap', 'opcua'],
                                        help="sets a protocol that will be cloned together with its dependencies")
parser.add_argument("-b", "--build", required=False, action="store_true",
                                     help="build the project and create a Makefile")
parser.add_argument("--path", default=HOME+"/Titan", required=False,
                              help="specify optionally your root directory, where all dependencies will be stored")
parser.add_argument("-e", "--executable_name", required=False, nargs=1,
                                               help="set the name of the executable that will be generated")
parser.add_argument("-v", "--verbose", required=False, action="store_true",
                                       help="progress status output is verbose")
args = parser.parse_args()

# base path for the Eclipse Titan protocol modules and test ports
PATH_BASE=args.path

# defined protocols
IOT_TESTWARE = {
    "coap":"CoAP",
    "mqtt":"MQTT",
    "opcua":"OPC_UA"
}

# version number of needed module
GIT_PROTOCOL_VERSION = {
    "coap":"f51e6415de7582d01bf725efdc5161d3533babd1",
    "mqtt":"c22560bb461c21cb1835f19721e990eb57691bad",
    "opcua":"f13b46d1c9c8448fee8e034c086d6fd3caedbd3b"
}

# current protocol
PROTOCOL = IOT_TESTWARE[args.protocol]

# default executable name
NAME_EXE = "iottestware_"+PROTOCOL
if args.executable_name!=None:
    NAME_EXE = args.executable_name[0]

# current working directory
project_dir = os.getcwd()

# Git flags
GIT_QUIET="--quiet"
if args.verbose:
    GIT_FLAG="--verbose"
else:
    GIT_FLAG=GIT_QUIET

""" INSTALLATION ! Do NOT change from here ! """

# These are prescribed in the *.tpd file
# TestPorts
PATH_SOCKET_API=PATH_BASE+"/TestPorts/Common_Components/Socket_API_CNL113686/"
PATH_IPL4=PATH_BASE+"/TestPorts/IPL4asp/"

# ProtocolModules
PATH_COMMON=PATH_BASE+"/ProtocolModules/COMMON/"
PATH_PROTOCOL=PATH_BASE+"/ProtocolModules/"+PROTOCOL+"/"

# Libraries
PATH_TCC=PATH_BASE+"/Libraries/TCCUsefulFunctions_CNL113472/"
PATH_IOTTESTWARE=PATH_BASE+"/IoT-Testware"
PATH_TW=PATH_IOTTESTWARE+"/iottestware."+args.protocol+"/"

# Git repositories
GIT_IOTTESTWARE = 'https://github.com/eclipse/iottestware.'+args.protocol+'.git'
GIT_SOCKET_API = 'https://github.com/eclipse/titan.TestPorts.Common_Components.Socket-API.git'
GIT_SOCKET_API_VERSION = '9e4ac13486f084e6eca74b976daf21b0028c44c1'
GIT_IPL4 = 'https://github.com/eclipse/titan.TestPorts.IPL4asp.git'
GIT_IPL4_VERSION = '8045145aa32cd4452f1acc30ade0a6ea79033bcc'
GIT_COMMON = 'https://github.com/eclipse/titan.ProtocolModules.COMMON.git'
GIT_COMMON_VERSION = '9a52b8dc609e18c193fbe4619aeb52d6c94e7922'
GIT_PROTOCOL = 'git://git.eclipse.org/gitroot/titan/titan.ProtocolModules.'+PROTOCOL+'.git'
GIT_TCC = 'https://github.com/eclipse/titan.Libraries.TCCUsefulFunctions.git'
GIT_TCC_VERSION = '27f76bb794af89f5ed9088317fc2e82247667f74'

def install(protocol):

    """"""""""""""""""""
    """ IOT-TESTWARE """
    """"""""""""""""""""
    if os.path.isdir(PATH_TW):
        print(PATH_TW + " already exists")
        os.chdir(PATH_TW)

        # ensure latest Titan version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_FLAG]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        # print sth ...
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_IOTTESTWARE, PATH_TW])

    print(" IoT-Testware ... done!")

    """"""""""""""""""
    """ TEST PORTS """
    """"""""""""""""""
    if os.path.isdir(PATH_SOCKET_API):
        print(PATH_SOCKET_API + " already exists")
        os.chdir(PATH_SOCKET_API)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_SOCKET_API, PATH_SOCKET_API]).communicate()[0]

        # go to PATH_SOCKET_API
        os.chdir(PATH_SOCKET_API)

    # checkout the required version SocketAPI
    subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_SOCKET_API_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    if os.path.isdir(PATH_IPL4):
        print(PATH_IPL4 + " already exists")
        os.chdir(PATH_IPL4)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_IPL4, PATH_IPL4]).communicate()[0]

        # go to PATH_IPL4
        os.chdir(PATH_IPL4)

    # checkout the required version IPL4asp
    subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_IPL4_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    print(" Test ports ... done!")

    """"""""""""""""""""""""
    """ PROTOCOL MODULES """
    """"""""""""""""""""""""
    if os.path.isdir(PATH_COMMON):
        print(PATH_COMMON + " already exists")
        os.chdir(PATH_COMMON)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_COMMON, PATH_COMMON]).communicate()[0]

        # go to PATH_COMMON
        os.chdir(PATH_COMMON)

    # checkout the required version of COMMON
    subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_COMMON_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    if os.path.isdir(PATH_PROTOCOL):
        print(PATH_PROTOCOL + " already exists")
        os.chdir(PATH_PROTOCOL)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_PROTOCOL, PATH_PROTOCOL]).communicate()[0]

        # go to PATH_PROTOCOL
        os.chdir(PATH_PROTOCOL)

    # checkout required version of Test Suite
    subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_PROTOCOL_VERSION[args.protocol]]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    print(" Protocol modules ... done!")

    """"""""""""""""""
    """ LIBRARIES  """
    """"""""""""""""""
    if os.path.isdir(PATH_TCC):
        print(PATH_TCC + " already exists")
        os.chdir(PATH_TCC)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_TCC, PATH_TCC]).communicate()[0]

        # go to PATH_TCC
        os.chdir(PATH_TCC)

    # checkout required version of TCC
    subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_TCC_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    print(" Libraries ... done!")
    print("Getting Dependencies done!")

    """"""""""""""""""""""""""
    """ PREPARE WORKSPACE  """
    """"""""""""""""""""""""""
    print("Preparing workspace ...")

    # clean the bin directory
    bin_folder = PATH_TW+"bin"
    if os.path.isdir(bin_folder):
        bin_files = glob.glob(bin_folder+"/*")
        for file in bin_files:
            os.remove(file)
    else:
        os.mkdir(bin_folder)

    print(" Bin directory clean!")


def build(protocol):
    bin_folder = PATH_TW+"bin"
    tpd_file = PATH_TW+"iottestware."+protocol+".tpd"

    # create bin folder if does not exist
    if not os.path.isdir(bin_folder):
        os.mkdir(bin_folder)

    # Create a Makefile with Titan's ttcn3_makefilegen
    # -f:           force overwriting of the output Makefile
    # -g:           generate Makefile for use with GNU make
    # -m:           always use makedepend for dependencies
    # -e ets_name:  name of the target executable
    # -t tpd:       read project descriptor file
    os.system("ttcn3_makefilegen -f -g -m -t "+tpd_file+" -e "+NAME_EXE+" "+PATH_TW+"src/*.ttcn")
    print("Makefile generated!")

    # move to bin folder
    os.chdir(bin_folder)

    # compile and build
    os.system("make compile")
    os.system("make")
    print("Compilation done!")
    print("Building the project done!")


def Main():
    print("Getting dependencies ...")
    install(args.protocol)
    if args.build:
        print("Building the project ...")
        build(args.protocol)

if __name__ == '__main__':
    Main()
