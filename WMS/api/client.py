import requests
'''
resp = requests.get("http://127.0.0.1:8000/api/products/")
'''
'''
resp = requests.post("http://127.0.0.1:8000/api/productcategory/",
	data={"name":"#$%","desc":"this is created post call"})
print resp
'''
#print resp.json()
# resp = requests.get("http://127.0.0.1:8000/api/productcategory/")
# print resp.json()
'''
resp = requests.put("http://127.0.0.1:8000/api/productcategory/1/",
	json={"name":"modifyied_pc1"})
print resp.json()

'''
'''
resp = requests.delete("http://127.0.0.1:8000/api/productcategory/4/",
	json={"name":"modifyied_pc1"})
if resp.status_code==204:
	print "deleted successfully"
else:
	print resp.json()
'''
resp = requests.get("http://127.0.0.1:8000/api/productcategory/3/")
print resp
