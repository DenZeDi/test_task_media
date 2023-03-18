# Тестовое задание

Задание:  
В каких ресторанах KFC аналитик может позавтракать в Новосибирске в 8:45.  

В данном каталоге лежит json файл с информацией о ресторанах KFC.  
Чтобы обработать эти данные и составить датафрейм необходимо запустить файл main.py

Далее чтобы произвести выгрузку, созданного dataframe, в базу данных, необходимо запустить файл db_update.py  
Получится файл df_location.db, для которого написан запрос для получения необходимой для выполнения задания информации:


select
    city, address, stl, etl
from
    df_location
where
    city = 'Новосибирск' and stl < '08:45' and bf = 1;

