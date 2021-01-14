# docker_pet_project_1


- Отправлять логи о неодачных попытках подключение к Linux серверам по ssh на удаленный сервер логирования (rsyslog)
- Каждые 10 минут данные о неудачных попытках с помощью Python записывать в базу данных Mysql, хранить эти данные в течении 30 дней.
- Выводить количество попыток на сайт(apache/php), разделить их на группы по дням.
- При привышение неудачных попытках в количестве 20 за период 1 час  прикрутить триггер на отправку уведомления на почту.




Prerequisite:



Client: 

echo 'auth.* @@192.168.50.91:514' > /etc/rsyslog.d/auth.conf
systemctl restart rsyslog




Server:

1) /mnt/data - Mounted external storage 
2) install docker / docker-compose
3) mkdir -p /mnt/data/{logs,mysql,out}
4) touch /mnt/data/out/outputlogs
