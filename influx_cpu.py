# -*- coding: utf-8 -*-
"""Tutorial on using the InfluxDB client."""
import psutil

import argparse
import time
import urllib2
import socket

from influxdb import InfluxDBClient

import  socket

hostName = socket.gethostname()

def main(host='localhost', port=8086,user = 'root',password = ''):
    """Instantiate a connection to the InfluxDB."""

    dbname = 'wemore'
    #dbuser = 'smly'
    #dbuser_password = 'my_secret_password'
    #query = 'select value from cpu_load_short;'
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
             	"host": ""
            },
            "fields": {
                "Float_value": 0.64,
                "value": 3,
            }
        }
    ]


    client = InfluxDBClient(host, port, user, password, dbname)
    print(client)
 

    while True:
        json_body[0]["fields"]["Float_value"]=psutil.cpu_percent(interval=None)
        json_body[0]["tags"]["host"]=hostName
        client.write_points(json_body)
        print("Write points: {0}".format(json_body))
        time.sleep(5)


    #print("Querying data: " + query)
    #result = client.query(query)
    #print("Result: {0}".format(result))


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    parser.add_argument('--user', type=str, required=False, default='root',
                        help='User of InfluxDB http API')
    parser.add_argument('--pass', type=str, required=False, default='',
                        help='pass of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port,user=args.user,pass=args.pass)

