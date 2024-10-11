export git_dir_name=JIRA-GPT
export GIT_USERNAME=lagairogo@gmail.com
export GIT_PASSWORD=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
export git_remote_url=https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/lagairogo-gai/${git_dir_name}.git

streamlit run main.py --server.port=8090 --server.address=0.0.0.0

