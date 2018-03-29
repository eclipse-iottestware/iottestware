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

parser = argparse.ArgumentParser(description='Installing and running the CoAP testsuite. Please specify a mode.')
parser.add_argument("-b", "--build", help="build the project and create an executable", action="store_true")
parser.add_argument("-e", "--execute", help="after the test suite built successfully it will be executed against a SUT", action="store_true")
parser.add_argument("-p", "--protocol", help="set a protocol you want to work with", choices=['mqtt', 'coap', 'opcua'], required=True)
args = parser.parse_args()

# defined protocols
IOT_TESTWARE = {
    "coap":"CoAP",
    "mqtt":"MQTT",
    "opcua":"OPC_UA"
}

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

# current protocol
PROTOCOL = IOT_TESTWARE[args.protocol]

# current working directory 
project_dir = os.getcwd()

# home directory
HOME = expanduser("~")

# base path for the Eclipse Titan protocol modules and test ports
PATH_BASE=HOME+"/Titan"

# Git flags
GIT_QUIET="--progress" # may remove this flag for a complete Git output

""" INSTALLATION ! Do NOT change from here ! """

# These are prescribed in the *.tpd file
# TestPorts
PATH_CORE=PATH_BASE+"/Core"
PATH_SOCKET_API=PATH_BASE+"/TestPorts/Common_Components/Socket_API_CNL113686/"
PATH_IPL4=PATH_BASE+"/TestPorts/IPL4asp/"

# ProtocolModules
PATH_COMMON=PATH_BASE+"/ProtocolModules/COMMON/"
PATH_PROTOCOL=PATH_BASE+"/ProtocolModules/"+PROTOCOL+"/"
# ... more protocols might follow


# Libraries
PATH_TCC=PATH_BASE+"/Libraries/TCCUsefulFunctions_CNL113472/"
PATH_IOTTESTWARE=PATH_BASE+"/IoT-Testware"
PATH_TW=PATH_IOTTESTWARE+"/iottestware."+args.protocol+"/"

def install(protocol):

    """"""""""""""""""
    """ TITAN CORE """
    """"""""""""""""""
    if os.path.isdir(PATH_CORE):
        print(PATH_CORE + " already exists")
        os.chdir(PATH_CORE)

        # ensure latest Titan version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/titan.core.git', PATH_CORE])

    """"""""""""""""""""
    """ IOT-TESTWARE """
    """"""""""""""""""""
    if os.path.isdir(PATH_TW):
        print(PATH_TW + " already exists")
        os.chdir(PATH_TW)

        # ensure latest Titan version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/iottestware.'+args.protocol+'.git', PATH_TW])


    """"""""""""""""""
    """ TEST PORTS """
    """"""""""""""""""
    if os.path.isdir(PATH_SOCKET_API):
        print(PATH_SOCKET_API + " already exists")
        os.chdir(PATH_SOCKET_API)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/titan.TestPorts.Common_Components.Socket-API.git', PATH_SOCKET_API]).communicate[0]

    if os.path.isdir(PATH_IPL4):
        print(PATH_IPL4 + " already exists")
        os.chdir(PATH_IPL4)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/titan.TestPorts.IPL4asp.git', PATH_IPL4]).communicate[0]


    """"""""""""""""""""""""
    """ PROTOCOL MODULES """
    """"""""""""""""""""""""
    if os.path.isdir(PATH_COMMON):
        print(PATH_COMMON + " already exists")
        os.chdir(PATH_COMMON)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/ProtocolModules.COMMON.git', PATH_COMMON]).communicate[0]

    if os.path.isdir(PATH_PROTOCOL):
        print(PATH_PROTOCOL + " already exists")
        os.chdir(PATH_PROTOCOL)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/ProtocolModules.'+PROTOCOL+'.git', PATH_PROTOCOL]).communicate[0]


    """"""""""""""""""
    """ LIBRARIES  """
    """"""""""""""""""
    if os.path.isdir(PATH_TCC):
        print(PATH_TCC + " already exists")
        os.chdir(PATH_TCC)

        # ensure latest version
        subprocess.Popen(['git', 'remote', 'update']).communicate()[0]
        subprocess.Popen(['git', 'checkout', GIT_QUIET, 'master']).communicate()[0]
        subprocess.Popen(['git', 'pull', GIT_QUIET]).communicate()[0]

        # back to cwd
        os.chdir(project_dir)
    else:
        subprocess.Popen(['git', 'clone', GIT_QUIET, 'https://github.com/eclipse/titan.Libraries.TCCUsefulFunctions.git', PATH_TCC]).communicate[0]


    """"""""""""""""""""""""""
    """ PREPARE WORKSPACE  """
    """"""""""""""""""""""""""
    # clean the bin directory
    bin_folder = PATH_TW+"bin"
    if os.path.isdir(bin_folder):
        bin_files = glob.glob(bin_folder+"/*")
        for file in bin_files:
            os.remove(file)
    else:
        os.mkdir(bin_folder)
    os.chdir(bin_folder)

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

    # Create a Makefile
    os.system("ttcn3_makefilegen -f -g -m -e CoAPTest *.ttcn *.hh *.cc")

# !MAY INCLUDE AN EXECUTION OPTION LATER!
#def execute():

def Main():
    if args.build:
        install(args.protocol)
    if not args.build and not args.execute:
        parser.print_help()

if __name__ == '__main__':
    Main()
