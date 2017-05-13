#!python3
# --------------------------------------------------------------------------------
# - Filename   : R3_MATRL_WERKS_ESTMJ_Extend.py
# - Description: Load Material Extensions / ESTMJ based on text file
#                Link Material to Spec.
#                Calling BAPI's
# - Author     : Gertjan Yspeert
# - Created    : 2017-05-09
# --------------------------------------------------------------------------------

from pyrfc import Connection
import os
from os.path import expanduser
import sys
import getopt
import csv
import datetime
from tqdm import tqdm
import pyodbc
import configparser
import keyring

r_conf = expanduser('~') + '\\PLM.cfg'

def load_map(mapfile):
    with open(mapfile, "r") as f:
        reader = csv.DictReader(f,delimiter='\t')
        result = {}
        for row in reader:
            key =  row['FILT_KEY']
            if key in result:
                pass
            result[key] = row['FILT_VALUE']
    return result

def process MARC_Ext():

        # result = connSAP.call('BAPI_MATERIAL_SAVEREPLICA',
                               # HEADDATA = data['HEADDATA'],
                               # CLIENTDATA = data['CLIENTDATA'],
                               # CLIENTDATAX = data['CLIENTDATAX'],
                               # PLANTDATA = data['PLANTDATA'],
                               # PLANTDATAX = data['PLANTDATAX'],




def main( argv):
    #OutDir = 'C:\\Temp\\lsmw\\'
    # DATAFILE = ''
    # outputdir = ''
    start_dt = datetime.datetime.now()
    try:
        opts, args = getopt.getopt( argv[1:],"he:",["help","env="])
    except getopt.GetoptError:
        print('\n usage R3_MATRL.py -e <environment>')
        sys.exit(2)
        
    p_env  = ''   # SAP environment, in configfile
    
    for opt, arg in opts:
        if opt == '-h':
            print('\n usage R3_MATRL.py -e <environment>')
            sys.exit()
        elif opt in ( "-e", "--env"):
            p_env = arg
    print(p_env)

    config = configparser.RawConfigParser()
    config.read(r_conf)
    params_connection = config._sections[p_env]
    params_connection['passwd'] = keyring.get_password(p_env,config.get(p_env, 'user'))
    connSAP = Connection(**params_connection)

    with open(DATAFILE, "r") as f:
    reader = csv.reader(f,delimiter='\t')
    partno = []
    next(reader)
    for row in reader:
        partno.append(row[0][0:row[0].rfind('_')])
    process_file(partno,OutDir)




if __name__ == "__main__":
    main(sys.argv)

