mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"skm39xb@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

pip install --upgrade pip
pip install -r requirements.txt
