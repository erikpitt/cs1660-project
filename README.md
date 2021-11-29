# cs1660-project

## Containers

* [Main Application Source Code](cs1660-project-main/main.py)
* [Main Application Docker Hub URL](https://hub.docker.com/r/erikjoy/cs1660-project-main)
* [Apache Hadoop Docker Hub URL](https://hub.docker.com/r/sequenceiq/hadoop-docker)
* [Apache Spark Docker Hub URL](https://hub.docker.com/r/bitnami/spark)
* [Jupyter Notebook Docker Hub URL](https://hub.docker.com/r/jupyter/base-notebook)
* [SonarQube Docker Hub URL](https://hub.docker.com/_/sonarqube)

## Deploying to a Local Kubernetes Cluster

1. Type git clone https://github.com/erikpitt/cs1660-project.git
2. Type cd cs1660-project
3. Type minikube start
4. Type kubectl apply -f hadoop/namenode-deployment.yaml
5. Type kubectl apply -f hadoop/namenode-service.yaml
6. Type kubectl apply -f hadoop/datanode-deployment.yaml
7. Type kubectl apply -f jupyter/jupyter-deployment.yaml
8. Type kubectl apply -f jupyter/jupyter-service.yaml
9. Type kubectl apply -f sonar/sonar-deployment.yaml
10. Type kubectl apply -f sonar/sonar-service.yaml
11. Type kubectl apply -f spark/spark-deployment.yaml
12. Type kubectl apply -f spark/spark-service.yaml
13. Open another terminal window and type minikube tunnel

## Pods and Services Running on Local Kubernetes Cluster

![](https://github.com/erikpitt/cs1660-project/blob/c76f7219cf6631cb423cce8b914f23f599a04d28/images/Local%20Kubernetes%20Cluster.png)

## Deploying to Google Kubernetes Engine

1. On Google Cloud Platform, navigate to Kubernetes Engine and click create and click configure next to GKE Autopilot. I named the cluster cs1660-project. Make sure the cluster is public and click create.
2. Once the cluster is created, click the name of the cluster and then click connect at the top.
3. Click run in cloud shell then press the enter key to execute the command. You'll likely see a popup where you have to click authorize.
4. Type git clone https://github.com/erikpitt/cs1660-project.git
5. Type cd cs1660-project
6. Type kubectl apply -f hadoop/namenode-deployment.yaml
7. Type kubectl apply -f hadoop/namenode-service.yaml
8. Type kubectl apply -f hadoop/datanode-deployment.yaml
9. Type kubectl apply -f jupyter/jupyter-deployment.yaml
10. Type kubectl apply -f jupyter/jupyter-service.yaml
11. Type kubectl apply -f sonar/sonar-deployment.yaml
12. Type kubectl apply -f sonar/sonar-service.yaml
13. Type kubectl apply -f spark/spark-deployment.yaml
14. Type kubectl apply -f spark/spark-service.yaml
15. Periodically type "kubectl get service -o wide" and wait until all the loadbalancers have received an external IP.
16. Using the search bar, navigate to External IP Addresses. Locate all of the external IP addresses of the loadbalances from the above command and reserve the four IP addresses so that they become static.
