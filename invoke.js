const { Lambda } = require("aws-sdk");

const lambda = new Lambda({
  apiVersion: "2015-03-31",
  region: "ap-southeast-2",
  // endpoint needs to be set only if it deviates from the default, e.g. in a dev environment
  // process.env.SOME_VARIABLE could be set in e.g. serverless.yml for provider.environment or function.environment
  endpoint: "http://localhost:3002",
});

const invokeLocalLambda = async function () {
  const params = {
    // FunctionName is composed of: service name - stage - function name, e.g.
    // FunctionName: "sls-poc-dev-hello-py",
    FunctionName: "sls-poc-dev-hello-python",
    InvocationType: "RequestResponse",
    Payload: JSON.stringify({ data: "foo" }),
  };

  const response = await lambda.invoke(params).promise();

  console.log(response);
};

invokeLocalLambda();
