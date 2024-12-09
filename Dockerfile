FROM vectorize-baseimg:latest

COPY --chown=1001:1001 --chmod=550 . /vectorize-agent/

USER root
RUN sed -i 's/umask 002/umask 027/g' /etc/bashrc && \
    sed -i 's/umask 022/umask 027/g' /etc/bashrc && \
    yum remove -y python3-pip gdb-gdbserver && \
    sh -c "find /usr /etc \( -name *yum* -o -name *dnf* -o -name *vi* \) -exec rm -rf {} + || true" && \
    sh -c "find /usr /etc \( -name ps -o -name top \) -exec rm -rf {} + || true" && \
    sh -c "rm -f /usr/bin/find /usr/bin/oldfind || true"

USER eulercopilot
WORKDIR /vectorize-agent
ENV PYTHONPATH=/vectorize-agent

CMD bash -c "python3 /vectorize-agent/vectorize_agent/app/app.py"
