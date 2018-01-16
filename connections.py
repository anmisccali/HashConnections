#Get list of hashes from Threatgrid that are shown in Investigate, print hashes and print network connections found in hashes.

import requests
import argparse
import investigate
import ConfigParser

parser = argparse.ArgumentParser(description="Pull in hash(es) from domain")
parser.add_argument('domain', help="Domain to look up")
parser.add_argument('--limit', default='100', help="Limit number returned, default is 100")
args = parser.parse_args()
sample_hash=[]
config = ConfigParser.ConfigParser()
config.read('config.ini')
api_key = config.get('auth', 'apikey')
inv = investigate.Investigate(api_key)
dom_query = inv.samples(args.domain, args.limit)
if dom_query['totalResults'] == 0:
	print 'No samples'
for q in dom_query:
	sample = dom_query['samples']
for s in sample:
	sha256 = s['sha256']
	if sha256 not in sample_hash:
		sample_hash.append(sha256)
for line in sample_hash:
	connections_query = inv.sample_connections(line)
	print ("\nHash: {0}\n".format(line))
	for item in connections_query['connections']:
		print (item['name'])
		if item['urls']:
			url = item['urls']
			print (url[0])
