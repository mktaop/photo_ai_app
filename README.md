Streamlit App that lets you take a picture and ask a multimodal large language model questions about it.
Requires Google API KEY.
If you want to deploy to Heroku, you will setup.sh and Procfile.  here they are.

setup.sh:
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

Procfile
