FROM debian:10
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo 'exit 0' > /usr/sbin/policy-rc.d
RUN apt-get update && apt install rsyslog -y
COPY rsyslog.conf /etc/
ENTRYPOINT ["rsyslogd", "-n", "-f", "/etc/rsyslog.conf"] 
EXPOSE 514

