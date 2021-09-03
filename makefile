# Install resources required for local setup.
.PHONY: init
init:
	npm i serverless serverless-offline
	./node_modules/.bin/serverless login
	docker network ls|grep df_network > /dev/null || docker network create aws_playground_network
	cd dotnet-lambdas && dotnet tool install -g Amazon.Lambda.Tools --framework netcoreapp3.1 || true && cd ..

# build the dotnet-lambdas .net project
.PHONY: build
build:
	cd dotnet-lambdas && ./build.sh && cd ..

# start serverless in docker
.PHONY: offline
offline:
	cd dotnet-lambdas && ./build.sh && cd ..
	AWS_PROFILE=default ./node_modules/.bin/serverless offline --stage local --useDocker --dockerNetwork aws_playground_network

# deploy lambda functions to sandbox
.PHONY: deploy-sandbox
deploy-sandbox:
	cd dotnet-lambdas && ./build.sh && cd ..
	AWS_PROFILE=default ./node_modules/.bin/serverless deploy --stage sandbox

# destroy lambda resources in sandbox
.PHONY: destroy-sandbox
destroy-sandbox:
	AWS_PROFILE=default ./node_modules/.bin/serverless remove --stage sandbox
