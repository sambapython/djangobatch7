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

resp = requests.get("http://127.0.0.1:8000/api/productcategory/3/")
print resp

resp = requests.post("http://127.0.0.1:8000/api/stockoperations/",
	json={"vendor":1,"operation_type":"i",
	"items":[{"product":1,"count":20},{"product":1,"count":30}],
	"name":"API stockop1","desc":"created by API"})
print resp
print resp.json()

resp = requests.post("http://127.0.0.1:8000/api/productcategoryser/",
	data={"name":"pcAPI1","desc":"this is created api call",
	"unique_name":"name1"})
print resp
print resp.json()

resp = requests.post("http://127.0.0.1:8000/api/stockoperationsser/",
	json={"vendor":10,"operation_type":"i",
	"items":[{"product":1,"count":20,"name":"l1"},
	{"product":1,"count":30,"name":"l2"}],
	"name":"API stockop1","desc":"created by API"})
print resp
print resp.json()


resp = requests.get("http://127.0.0.1:8000/api/stockoperationsser/")
print resp
print resp.json()
'''
resp = requests.post("http://127.0.0.1:8000/api/productcategory/",
	data={"name":"pc1","desc":"this is created post call",
	"unique_name":"pc1"})
print resp

