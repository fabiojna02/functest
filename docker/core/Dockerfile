FROM alpine:3.9

ARG BRANCH=master
ARG OPENSTACK_TAG=master
ARG PIP_TAG=18.0

RUN apk --no-cache add --update \
        python libffi openssl libjpeg-turbo py-pip bash \
        grep sed wget ca-certificates git openssh-client qemu-img && \
    apk --no-cache add --virtual .build-deps --update \
        python-dev build-base linux-headers libffi-dev \
        openssl-dev libjpeg-turbo-dev && \
    wget -q -O- https://git.opnfv.org/functest/plain/upper-constraints.txt?h=$BRANCH > upper-constraints.opnfv.txt  && \
    sed -i -E /#egg=functest/d upper-constraints.opnfv.txt && \
    pip install --no-cache-dir --src /src -cupper-constraints.opnfv.txt \
        -chttps://opendev.org/openstack/requirements/raw/branch/$OPENSTACK_TAG/upper-constraints.txt \
        pip==$PIP_TAG && \
    pip install --no-cache-dir --src /src -cupper-constraints.opnfv.txt \
        -chttps://opendev.org/openstack/requirements/raw/branch/$OPENSTACK_TAG/upper-constraints.txt \
        -e git+https://opendev.org/openstack/requirements@$OPENSTACK_TAG#egg=openstack_requirements && \
    git init /src/functest && \
    (cd /src/functest && \
        git fetch --tags https://gerrit.opnfv.org/gerrit/functest $BRANCH && \
        git checkout FETCH_HEAD) && \
    update-requirements -s --source /src/openstack-requirements /src/functest && \
    pip install --no-cache-dir --src /src -cupper-constraints.opnfv.txt \
        -chttps://opendev.org/openstack/requirements/raw/branch/$OPENSTACK_TAG/upper-constraints.txt \
        /src/functest && \
    rm -r upper-constraints.opnfv.txt /src/functest && \
    cp /usr/lib/python2.7/site-packages/functest/ci/logging.ini /usr/lib/python2.7/site-packages/xtesting/ci/ && \
    cp /usr/lib/python2.7/site-packages/functest/ci/logging.debug.ini /usr/lib/python2.7/site-packages/xtesting/ci/ && \
    bash -c "mkdir -p /var/lib/xtesting /home/opnfv" && \
    ln -s /var/lib/xtesting /home/opnfv/functest && \
    bash -c "mkdir -p /home/opnfv/functest{/conf,/data,/images,/results} /home/opnfv/repos/vnfs" && \
    apk del .build-deps
