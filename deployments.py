from kubernetes import client, config
from kubernetes.client import configuration
import sys


def main():
	contexts, active_context = config.list_kube_config_contexts()
	if not contexts:
		print("Cannot find any context in kube-config file.")
		return
	config.load_kube_config(context=active_context["name"])
	api = client.AppsV1Api()
	if len(sys.argv) == 1 :
		ret=api.list_deployment_for_all_namespaces()
		print ("List deployments for all namespaces")
	else:
		ret = api.list_namespaced_deployment(namespace= sys.argv[1])
		print ("List deployments for " +  sys.argv[1] + " namespace" )
	max_name_length = 4
	for item in ret.items:
		if len(item.metadata.name) > max_name_length:
			max_name_length = len(item.metadata.name) 
	max_name_length +=1		
	print ("NAME".ljust(max_name_length) + "DATE                       IMAGES" )
	for item in ret.items:
		print (item.metadata.name.ljust(max_name_length)  + str(item.status.conditions[0].last_update_time) + "  " + item.spec.template.spec.containers[0].image )
		for container in item.spec.template.spec.containers[1:]:
			print ((" " * (max_name_length + 2 + len(str(item.status.conditions[0].last_update_time)))) + container.image)


if __name__ == '__main__':
	main()