FROM debian:10
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo 'exit 0' > /usr/sbin/policy-rc.d
RUN apt-get clean && apt-get update && apt-get install -y cron
COPY cron /etc/cron.d/cron
COPY del.sh /home/
RUN chmod +x /home/del.sh
RUN touch /var/log/cron.log
RUN chmod 0644 /etc/cron.d/cron
CMD ["/bin/bash", "-c", "cron && tail -f /var/log/cron.log"]
