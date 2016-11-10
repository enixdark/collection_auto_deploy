##config some envs in config.py,then generate yaml file by command:
`make generate` or `python setup.py generate`

##remove all yaml file by command:
`make clean` or `python setup.py clean`

## create namespace for example if not exists
`kuberctl create namespace example`

## create secret key with docker registry 
`kubectl create secret docker-registry [key] --docker-username=[username] --docker-password=[password] --docker-email=[email]`
 
use docker login to login to private docker-registry

`docker login`

get encrypt token from docker config after login

`cat ~/.docker/config.json | base64`

save token and replace it into data..dockerconfigjson in example-secret.yml file` 

## create Docker-registry secrets
`kubectl create -f example-secret.yaml`
cat ~/.docker/config.json | base64

## create Persistent Volumes
`kubectl create -f pv-*.yaml`

## create Persistent Volume Claim
`kubectl create -f pvc-*.yaml`

## create all ReplicationControllers (RC) and Services (SVC) objects
`kubectl create -f <others>.yaml`

## create service , rc from image
`kubectl create -f [folder_name]/.`

## to delete all service, rc, pv, pvc in etcd use
`kubectl delete --all deployment,rc,pods,svc,pv,pvc,hpa --namespace=example`


