#path: ./init.sh

# 1. Create a virtual environment
set -o allexport
source .env 
set +o allexport

# 2. Install requirements
pip install -r requirements.txt --no-cache-dir --upgrade #do not use cache dir
mkdir -p ./.datalake #create datalake folder
kaggle datasets download -d jpmiller/layoutlm -p ./.datalake/ --unzip #download layoutlm model

