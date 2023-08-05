
# *******
# airflow
# https://velog.io/@jenori_dev/airflow-%EB%A7%A5-%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%EC%97%90%EC%96%B4%ED%94%8C%EB%A1%9C%EC%9A%B0-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
# https://arpitrana.medium.com/install-airflow-on-macos-guide-fc66399b2a9e
conda create -n [가상환경이름]_env python=3.7
source activate [가상환경이름]_env
pip3 install apache-airflow
airflow users create -u admin -p admin -f euiyoung -l hwang -r Admin -e admin@admin.com
airflow db init
#/Users/euiyoung.hwang/airflow (cd ~/airflow)
airflow webserver -p 8889
#(admin/admin)

#sample_task = BashOperator(
#    task_id="sample_task",
#    bash_command='python3 sample_task.py',
#    dag=dag)

#default_timezone = utc
#default_timezone = America/Chicag

less ~/airflow/airflow.cfg
# subfolder in a code repository. This path must be absolute.
#dags_folder = /Users/euiyoung.hwang/airflow/dags
#dags_folder = /Users/euiyoung.hwang/ES/Python_Workspace/ES_Docker/Airflow/dags

airflow tasks test hello_world hello_task

# markupsafe error
pip install markupsafe==2.0.1
# Update the airflow.cfg file. Search for the variable dagbag_import_timeout and update it's value type to integer instead of float, from dagbag_import_timeout = 30.0 to dagbag_import_timeout = 30. This should work fine.
# *******
