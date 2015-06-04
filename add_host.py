#!/usr/bin/python
import urllib2,json,common,web

urls=(
	'/add_host','Add',
)
render = web.template.render('templates')

class Add:
	def GET(self):
		data = web.input()
		ip,group,template = data['ip'],data['group'],data['template']
		if ip and group and template:
			host = common.get_hostid(ip)
			if not common.check_host_exists(ip):
				common.add_host(ip,10050,group,template)
				return render.add_host()
			else:
				return render.add_host_error()
		

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
