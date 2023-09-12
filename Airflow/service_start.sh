#!/bin/bash
set -e

# SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
# cd $SCRIPTDIR

source /Users/euiyoung.hwang/opt/anaconda3/bin/activate airflow
airflow webserver -p 8889
