cd infra/cdk

export ACCOUNT_NUMBER="$1"

npm install -g aws-cdk
pip install -r requirements.txt

cdk deploy --ci
