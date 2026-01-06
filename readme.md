 docker run -d --name postgres-server -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin123 -e POSTGRES_DB=billing_db -p 5432:5432 -v ${PWD}/pgdata:/var/lib/postgresql/data postgres:16




GIT_SSH_COMMAND='ssh -i ~/.ssh/github_deploy' git clone git@github.com:franciscohiguera1975/posts_api.git /opt/posts_api

