const { Lambda } = require("aws-sdk");

const lambda = new Lambda({
  apiVersion: "2015-03-31",
  region: "ap-southeast-2",
  endpoint: "http://localhost:3002",
});

const invokeLocalLambda = async function () {
  const params = {
    // FunctionName is composed of: service name - stage - function name, e.g.
    FunctionName: "sls-poc-dev-hello-python",
    InvocationType: "RequestResponse",
    Payload: JSON.stringify({ data: "foo" }),
  };

  const response = await lambda.invoke(params).promise();
  const payload = JSON.parse(response.Payload);
  console.log(payload);
};

invokeLocalLambda();
