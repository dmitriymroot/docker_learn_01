FROM debian:10
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo 'exit 0' > /usr/sbin/policy-rc.d
RUN apt-get clean && apt-get update && apt-get install -y cron
COPY cron /etc/cron.d/cron
COPY writebd.py /home/
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install pymysql
RUN touch /var/log/cron.log
RUN chmod +x /home/writebd.py
RUN chmod 0644 /etc/cron.d/cron
CMD ["/bin/bash", "-c", "cron && tail -f /var/log/cron.log"]

