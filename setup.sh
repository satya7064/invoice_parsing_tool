mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

echo "\
[easyocr]\n\
download_enabled = false\n\
\n\
" > ~/.streamlit/secrets.toml
