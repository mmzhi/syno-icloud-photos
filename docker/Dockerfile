FROM python:3.7

ARG ICLOUDPD_VERSION=1.4.3
RUN set -xe \
  && apt-get update && apt-get -y install cron \
  && pip install icloudpd==${ICLOUDPD_VERSION} schedule \
  && icloudpd --version \
  && icloud -h | head -n1

ADD run.py /usr/bin/

RUN chmod +x /usr/bin/run.py

WORKDIR /usr/bin

CMD ["python", "run.py"]