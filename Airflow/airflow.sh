
# *******
# airflow
# https://velog.io/@jenori_dev/airflow-%EB%A7%A5-%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%EC%97%90%EC%96%B4%ED%94%8C%EB%A1%9C%EC%9A%B0-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
conda create -n [가상환경이름]_env python=3.7
source activate [가상환경이름]_env
pip3 install apache-airflow
airflow users create -u admin -p admin -f euiyoung -l hwang -r Admin -e admin@admin.com
airflow db init
#/Users/euiyoung.hwang/airflow (cd ~/airflow)
airflow webserver -p 8889
#(admin/admin)

less ~/airflow/airflow.cfg
# subfolder in a code repository. This path must be absolute.
#dags_folder = /Users/euiyoung.hwang/airflow/dags
#dags_folder = /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Airflow/dags
# *******
