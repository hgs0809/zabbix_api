#!/usr/bin/python
import urllib2,json

url='http://0.0.0.0/api_jsonrpc.php'
user_pass={'username':'xxxxxxx','password':'xxxxxxxxx'}
header={"Content-Type":"application/json"}

def get_auth():
	data = json.dumps({
		"jsonrpc":"2.0",
		"method":"user.login",
		"params":{
			"user":user_pass['username'],
			"password":user_pass['password']
			},
	"id":0
	}
	)
	
	request = urllib2.Request(url,data)
	for key in header:
		request.add_header(key,header[key])

	try:
		result = urllib2.urlopen(request)
	except urllib2.URLError as e:
		return None
	else:
		response = json.loads(result.read())
		result.close()
		#print "Auth Successful. The Auth ID ia",response['result']
		return response['result']


def get_data(url,method,params):
	data = json.dumps(
		{
			"jsonrpc":'2.0',
			"method":method,
			"params":params,
			"auth":get_auth(),
			"id":1,
		}
	)
	request = urllib2.Request(url,data)
	for key in header:
		request.add_header(key,header[key])
	try:
		result = urllib2.urlopen(request)
	except urllib2.URLError as e:
		return e
	else:
		response = json.loads(result.read())
		result.close()
		#print response
		return response['result']

def add_host(ip,port,groupid,templateid):
	method = "host.create"
	params = {'host': ip, 'interfaces': [{'ip': ip, 'useip': 1, 'dns': '', 'main': 1, 'type': 1, 'port': port}], 'groups': [{'groupid': groupid}],'templates': [{'templateid': templateid}]}
		
	all_data = get_data(url,method,params)
	return all_data
def check_host_exists(host_name):
	method = "host.exists"
	params = {"host":host_name}
	all_data = get_data(url,method,params)
	return all_data

def get_hostid(ip):
        method = "hostinterface.get"
        params = {"output":"extend","filter":{"ip":ip}}
        all_data = get_data(url,method,params)
        return all_data


if __name__ == '__main__':
	print 'ok'
	#parser = argparse.ArgumentParser(description="add zabbix host")
	#parser.add_argument("--ip",metavar="ip",dest='ip',required=True,help="server ip")
	#parser.add_argument("--port",metavar="port",dest='port',default=10050,help="zabbix agent port default is 10050")
	#parser.add_argument("--groupid",metavar="groupid",dest='groupid',default=2,help="server group default is Bj-ZhaoWei-Idc")
	#parser.add_argument("--templateid",metavar="templateid",dest='templateid',default=10098,help="link templdate default is 'Template OS Linux'")
	#args = parser.parse_args()
	#ip = args.ip
	#port = args.port
	#groupid = args.groupid
	#templateid = args.templateid
	#host = get_hostid(ip)
	#if not check_host_exists(ip):
	#	add_host(ip,port,groupid,templateid)
