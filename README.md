


# requirements
1. kaggle.json to use in .env
> this is to be retrieved 
>To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'. This will trigger the download of kaggle.json, a file containing your API credentials.
2. openai api key
3. git and [git-lfs](https://git-lfs.com/)
macos
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# and run something similar to found in the output
# (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/suchattangjarukij/.zprofile
#eval "$(/opt/homebrew/bin/brew shellenv)"
brew install git-lfs
```
windows
>I dont have any/ to be added
4. Chatbot requirement 
>To run chat bot with openai all the needed requirement are in requirement file

# init
1. copy .env.example to .env
```bash
cp .env.example .env
```
2. edit .env
```bash
KAGGLE_USERNAME=your_user_name_without_quotes
KAGGLE_KEY=your_key_without_quotes
OPENAI_API_KEY=sk-1234
```
3. download dataset from kaggle and install the python packages 
```bash
sh init.sh
```

# run

```python
streamlit run main.py
```

>To run chatbot with openai
>```
>streamlit run chatbot.py

>for certain someone with bash difficulties
>```
>python -m streamlit run main.py
>```


# Goals
1. use LLM to generate response
2. Response Generation Frame


# Tasks
1. [ ] create and share folder on onedrive 
    - [ ] slides 
2. [ ] system archecture
    - [ ] pipeline 
3. [ ] demo of the whole proces without external DB
4. [ ] number of diff frame
5. [ ] auth 

save
```json
{
    "problem":str,
    "prompt":str,
    "task":str (GPT4, GPT4withTOT, GPT4withDB)
    "response":str,
    "feedback": str,
    "timestamp and metadata": {}
    
}

```
