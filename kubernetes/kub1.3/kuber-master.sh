export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt)
export ARCH=amd64
# docker run -d \
#     --volume=/:/rootfs:ro \
#     --volume=/sys:/sys:rw \
#     --volume=/var/lib/docker/:/var/lib/docker:rw \
#     --volume=/var/lib/kubelet/:/var/lib/kubelet:rw \
#     --volume=/var/run:/var/run:rw \
#     --net=host \
#     --pid=host \
#     --privileged \
#     gcr.io/google_containers/hyperkube-${ARCH}:${K8S_VERSION} \
#     /hyperkube kubelet \
#         --containerized \
#         --hostname-override=127.0.0.1 \
#         --address=0.0.0.0 \
#         --api-servers=http://localhost:8080 \
#         --config=/etc/kubernetes/manifests \
#         --cluster-dns=10.0.0.10 \
#         --cluster-domain=cluster.local \
#         --allow-privileged --v=2

  # gcr.io/google_containers/hyperkube-${ARCH}:${K8S_VERSION} \

# docker run \
#   --volume=/:/rootfs:ro \
#   --volume=/sys:/sys:ro \
#   --volume=/dev:/dev \
#   --volume=/var/lib/docker/:/var/lib/docker:ro \
#   --volume=/var/lib/kubelet/:/var/lib/kubelet:rw \
#   --volume=/var/run:/var/run:rw \
#   --net=host \
#   --pid=host \
#   --privileged=true \
#   -d \
#   gcr.io/google_containers/hyperkube:v1.0.1 \
#   /hyperkube kubelet --containerized --hostname-override="127.0.0.1" --address="0.0.0.0" --api-servers=http://localhost:8080 --config=/etc/kubernetes/manifests

docker run -d \
    --volume=/:/rootfs:ro \
    --volume=/sys:/sys:rw \
    --volume=/var/lib/docker/:/var/lib/docker:rw \
    --volume=/var/lib/kubelet/:/var/lib/kubelet:rw \
    --volume=/var/run:/var/run:rw \
    --net=host \
    --pid=host \
    --privileged \
    gcr.io/google_containers/hyperkube-${ARCH}:${K8S_VERSION} \
    /hyperkube kubelet \
        --containerized \
        --hostname-override=127.0.0.1 \
        --address=0.0.0.0 \
        --api-servers=http://localhost:8080 \
        --config=/etc/kubernetes/manifests \
        --allow-privileged --v=2