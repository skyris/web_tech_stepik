def application(environ, start_response):
	query_string = environ['QUERY_STRING']
  	query_list = query_string.split("&")
  	start_response('200 OK', [('Content-Type', 'text/plain')])
  	return ["\n".join(query_list)]