FROM opnfv/functest-tempest

ARG BRANCH=master
ARG OPENSTACK_TAG=master

COPY thirdparty-requirements.txt thirdparty-requirements.txt
RUN apk --no-cache add --update python3 sshpass && \
    apk --no-cache add --virtual .build-deps --update \
        python-dev python3-dev build-base linux-headers libffi-dev \
        openssl-dev libjpeg-turbo-dev file && \
    wget -q -O- https://opendev.org/openstack/requirements/raw/branch/$OPENSTACK_TAG/upper-constraints.txt > upper-constraints.txt && \
    sed -i -E s/^tempest==+.*$/-e\ git+https:\\/\\/opendev.org\\/openstack\\/tempest#egg=tempest/ upper-constraints.txt && \
    wget -q -O- https://git.opnfv.org/functest/plain/upper-constraints.txt?h=$BRANCH > upper-constraints.opnfv.txt && \
    sed -i -E /#egg=functest/d upper-constraints.opnfv.txt && \
    pip install --no-cache-dir --src /src -cupper-constraints.txt \
        -cupper-constraints.opnfv.txt \
        -rthirdparty-requirements.txt && \
    python3 -m pip install --no-cache-dir --src /src -cupper-constraints.txt \
        -cupper-constraints.opnfv.txt \
        -rthirdparty-requirements.txt && \
    rm -r upper-constraints.txt upper-constraints.opnfv.txt thirdparty-requirements.txt && \
    apk del .build-deps
COPY testcases.yaml /usr/lib/python2.7/site-packages/xtesting/ci/testcases.yaml
CMD ["run_tests", "-t", "all"]
