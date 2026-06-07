PS D:\cicdproject> ls


    Directory: D:\cicdproject


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          6/6/2026  10:47 AM          20283 CICD Pipeline with Docker GitHub Actions Docker Hub and Kubernetes.docx


PS D:\cicdproject>
PS D:\cicdproject> docker build -t flask-app:v1 .
[+] Building 43.3s (11/11) FINISHED                                                                             docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                            0.3s
 => => transferring dockerfile: 198B                                                                                            0.1s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                             4.5s
 => [auth] library/python:pull token for registry-1.docker.io                                                                   0.0s
 => [internal] load .dockerignore                                                                                               0.1s
 => => transferring context: 2B                                                                                                 0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a9fc0e6e38295747e49ac0       9.7s
 => => resolve docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a9fc0e6e38295747e49ac0       0.2s
 => => sha256:797d495f2c68eb4664df918d39078ca04612d7ef47c57b5c784f7f6eedd42bf5 14.37MB / 14.37MB                                4.9s
 => => sha256:45006ceeeea9e2ca59a046b6f4ac9a212e4b27b3d8d6e7d348b03f0aaccdac99 250B / 250B                                      1.1s
 => => sha256:8649771fee179d7c2590c94f533aaa5fceb70e36e25dec83672fe836d99577c5 1.29MB / 1.29MB                                  2.1s
 => => extracting sha256:8649771fee179d7c2590c94f533aaa5fceb70e36e25dec83672fe836d99577c5                                       1.9s
 => => extracting sha256:797d495f2c68eb4664df918d39078ca04612d7ef47c57b5c784f7f6eedd42bf5                                       4.2s
 => => extracting sha256:45006ceeeea9e2ca59a046b6f4ac9a212e4b27b3d8d6e7d348b03f0aaccdac99                                       0.1s
 => [internal] load build context                                                                                               0.3s
 => => transferring context: 21.14kB                                                                                            0.1s
 => [2/5] WORKDIR /app                                                                                                          0.7s
 => [3/5] COPY requirements.txt .                                                                                               0.4s
 => [4/5] RUN pip install -r requirements.txt                                                                                  21.2s
 => [5/5] COPY . .                                                                                                              0.2s
 => exporting to image                                                                                                          5.3s
 => => exporting layers                                                                                                         3.3s
 => => exporting manifest sha256:476bf8ceeba7e269593ea342b19447be00653da2ba4637858b362a49c431e119                               0.0s
 => => exporting config sha256:f457d8e673316998fd9df4ebecce00b81e88cc40e02b2f5422a59482dd49c997                                 0.0s
 => => exporting attestation manifest sha256:9f67a17e23736e4646c1b07794250b7fe57b8cba27bcafe863e0706a34838fc4                   0.1s
 => => exporting manifest list sha256:41a774991f53dc78cbfd6f0a34bc1d2669ae4e3bfba9b5cc76bee841d41dd4bb                          0.1s
 => => naming to docker.io/library/flask-app:v1                                                                                 0.0s
 => => unpacking to docker.io/library/flask-app:v1                                                                              1.6s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/d2vhy6727bjfp13lle1j27bwp
PS D:\cicdproject>
PS D:\cicdproject> docker run -p 5000:5000 flask-app:v1
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [06/Jun/2026 18:08:11] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [06/Jun/2026 18:08:13] "GET /favicon.ico HTTP/1.1" 404 -
PS D:\cicdproject> docker login
Authenticating with existing credentials... [Username: rajsingh9479]

i Info → To login with a different account, run 'docker logout' followed by 'docker login'


Login Succeeded
PS D:\cicdproject> docker tag flask-app:v1 rajsingh9479/flask-cicd:v1
PS D:\cicdproject> docker push docker tag flask-app:v1 rajsingh9479/flask-cicd:v1
docker: 'docker push' requires 1 argument

Usage:  docker push [OPTIONS] NAME[:TAG]

Run 'docker push --help' for more information
PS D:\cicdproject> docker push docker tag flask-app:v1 rajsingh9479/flask-cicd:v1^C
PS D:\cicdproject>
PS D:\cicdproject> docker push rajsingh9479/flask-cicd:v1
The push refers to repository [docker.io/rajsingh9479/flask-cicd]
1ee0664b9a12: Pushed
06868912ee09: Pushed
8649771fee17: Pushed
1a7719028189: Pushed
797d495f2c68: Pushed
45006ceeeea9: Pushed
6667c126342d: Pushed
5b4d6ff92fc4: Pushed
45a19b3ba496: Pushed
v1: digest: sha256:41a774991f53dc78cbfd6f0a34bc1d2669ae4e3bfba9b5cc76bee841d41dd4bb size: 856
PS D:\cicdproject> kind create cluster --name cicd-cluster
Creating cluster "cicd-cluster" ...
 • Ensuring node image (kindest/node:v1.31.0) 🖼  ...
 ✓ Ensuring node image (kindest/node:v1.31.0) 🖼
 • Preparing nodes 📦   ...
 ✓ Preparing nodes 📦
 • Writing configuration 📜  ...
 ✓ Writing configuration 📜
 • Starting control-plane 🕹️  ...
 ✓ Starting control-plane 🕹️
 • Installing CNI 🔌  ...
 ✓ Installing CNI 🔌
 • Installing StorageClass 💾  ...
 ✓ Installing StorageClass 💾
Set kubectl context to "kind-cicd-cluster"
You can now use your cluster with:

kubectl cluster-info --context kind-cicd-cluster

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
PS D:\cicdproject> kubectl get nodes
NAME                         STATUS   ROLES           AGE   VERSION
cicd-cluster-control-plane   Ready    control-plane   62s   v1.31.0
PS D:\cicdproject> kubectl get pods
No resources found in default namespace.
PS D:\cicdproject> kubectl get events


PS D:\cicdproject> kubectl get pods
No resources found in default namespace.
PS D:\cicdproject>
PS D:\cicdproject> kubectl get nodes
NAME                         STATUS   ROLES           AGE     VERSION
cicd-cluster-control-plane   Ready    control-plane   2m17s   v1.31.0
PS D:\cicdproject>
PS D:\cicdproject> kubectl apply -f deployment.yaml
error: the path "deployment.yaml" does not exist
PS D:\cicdproject>
PS D:\cicdproject> kubectl apply -f service.yaml
error: the path "service.yaml" does not exist
PS D:\cicdproject> kubectl apply -f deployment.yml
deployment.apps/flask-app created
PS D:\cicdproject> kubectl apply -f .\service.yml
service/flask-service created
PS D:\cicdproject> kubectl get nodes
NAME                         STATUS   ROLES           AGE     VERSION
cicd-cluster-control-plane   Ready    control-plane   4m57s   v1.31.0
PS D:\cicdproject> kubectl get pods
NAME                         READY   STATUS             RESTARTS   AGE
flask-app-6db864d755-25bbd   0/1     ImagePullBackOff   0          25s
flask-app-6db864d755-5tlzh   0/1     ImagePullBackOff   0          25s
flask-app-6db864d755-r9l5q   0/1     ImagePullBackOff   0          25s
PS D:\cicdproject> kubectl get svc
NAME            TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
flask-service   NodePort    10.96.3.203   <none>        80:30885/TCP   25s
kubernetes      ClusterIP   10.96.0.1     <none>        443/TCP        5m5s
PS D:\cicdproject>