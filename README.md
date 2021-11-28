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
2. cd into the repository
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
