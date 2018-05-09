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

# modules needed by every protocol
IOT_TESTWARE_MODULES = {
    "coap":["src/negative_testing/CoAP_EncDec.cc",
        "src/negative_testing/CoAP_Types.ttcn"],
    "mqtt":["src/negative_testing/MQTT_v3_1_1_Types.ttcn",
        "src/negative_testing/MQTT_v3_1_1_IPL4SizeFunction.ttcn",
        "src/negative_testing/MQTT_v3_1_1_EncDec.cc",
        "src/negative_testing/MQTT_v3_1_1_Size.cc"],
    "opcua": ["src/OpcUa_Common.ttcn",
        "src/OpcUa_Templates_Binary.ttcn",
        "src/OpcUA_Types_Binary.ttcn"]
}

# version number of needed module
GIT_PROTOCOL_VERSION = {
    "coap":"8e47e5abb89b88fcbe0d42f6372d940e495fdb62",
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
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_SOCKET_API_VERSION]).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_SOCKET_API, PATH_SOCKET_API]).communicate()[0]

        # go to PATH_SOCKET_API and checkout the required version
        os.chdir(PATH_SOCKET_API)
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_SOCKET_API_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    if os.path.isdir(PATH_IPL4):
        print(PATH_IPL4 + " already exists")
        os.chdir(PATH_IPL4)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_IPL4_VERSION]).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_IPL4, PATH_IPL4]).communicate()[0]

        # go to PATH_IPL4 and checkout the required version
        os.chdir(PATH_IPL4)
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
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_COMMON_VERSION]).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_COMMON, PATH_COMMON]).communicate()[0]

        # go to PATH_COMMON and checkout the required version
        os.chdir(PATH_COMMON)
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_COMMON_VERSION]).communicate()[0]

    # back to cwd
    os.chdir(project_dir)

    if os.path.isdir(PATH_PROTOCOL):
        print(PATH_PROTOCOL + " already exists")
        os.chdir(PATH_PROTOCOL)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_PROTOCOL_VERSION[args.protocol]]).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_PROTOCOL, PATH_PROTOCOL]).communicate()[0]

        # go to PATH_PROTOCOL and checkout the required version
        os.chdir(PATH_PROTOCOL)
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
        subprocess.Popen(['git', 'checkout', GIT_QUIET, GIT_TCC_VERSION]).communicate()[0]
    else:
        subprocess.Popen(['git', 'clone', GIT_FLAG, GIT_TCC, PATH_TCC]).communicate()[0]

        # go to PATH_TCC and checkout the required version
        os.chdir(PATH_TCC)
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
    os.chdir(bin_folder)
    print(" Bin directory clean!")

    # Create symlinks inside the bin folder to create a Makefile in the next step
    os.symlink(PATH_COMMON + "/src/General_Types.ttcn", "General_Types.ttcn")

    # link to IPL4asp TestPort
    os.symlink(PATH_IPL4 + "/src/IPL4asp_Types.ttcn", "IPL4asp_Types.ttcn")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_Functions.ttcn", "IPL4asp_Functions.ttcn")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_PortType.ttcn", "PortType.ttcn")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_PT.cc", "IPL4asp_PT.cc")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_PT.hh", "IPL4asp_PT.hh")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_protocol_L234.hh", "IPL4asp_protocol_L234.hh")
    os.symlink(PATH_IPL4 + "/src/IPL4asp_discovery.cc", "IPL4asp_discovery.cc")

    # link to Socket_API_CNL113686 TestPort
    os.symlink(PATH_SOCKET_API + "/src/Socket_API_Definitions.ttcn", "Socket_API_Definitions.ttcn")

    # link to TTC Library
    os.symlink(PATH_TCC + "/src/TCCInterface_Functions.ttcn", "TCCInterface_Functions.ttcn")
    os.symlink(PATH_TCC + "/src/TCCInterface_ip.h", "TCCInterface_ip.h")
    os.symlink(PATH_TCC + "/src/TCCInterface.cc", "TCCInterface.cc")
    os.symlink(PATH_TCC + "/src/TCCConversion_Functions.ttcn", "TCCConversion_Functions.ttcn")
    os.symlink(PATH_TCC + "/src/TCCConversion.cc", "TCCConversion.cc")

    # link to protocol files
    for file in IOT_TESTWARE_MODULES[args.protocol]:
        os.symlink(PATH_PROTOCOL+file, os.path.basename(file))


    # link to IoT-Testware modules
    src_dir = glob.glob(PATH_TW+"/src/*")
    for file in src_dir:
        os.symlink(file, os.path.basename(file))

    print(" Symlinks created successfully!")
    print("Finished! Everything set up.")


def build():
    bin_folder = PATH_TW+"bin"
    # check if needed files are linked to bin folder
    if not os.path.isdir(bin_folder):
        print("bin folder does not exist. Please run the script again with '-b' or '--build' flag before.")
        parser.print_help()
        return

    os.chdir(bin_folder)

    # Create a Makefile
    os.system("ttcn3_makefilegen -f -g -m -e "+NAME_EXE+" *.ttcn *.hh *.cc")
    print("Makefile generated!")

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
        build()

if __name__ == '__main__':
    Main()
