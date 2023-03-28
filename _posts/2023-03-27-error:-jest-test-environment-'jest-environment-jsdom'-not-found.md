---
layout: post
title: "Error: Jest Test Environment 'jest-environment-jsdom' Not Found"
tags: ['javascript', 'node.js', 'typescript', 'jestjs', 'ts-jest']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When running tests with Jest, you may encounter an error stating that the `jest-environment-jsdom` environment is not found. This error can occur for several reasons. In this article, we'll discuss what this error means, and how to troubleshoot it. 

## What is Jest?

Jest is a popular JavaScript testing framework created by Facebook. It allows developers to write tests for their code in an easy-to-read syntax. Jest also provides a number of features, such as mocking, assertion libraries, and snapshot testing. 

## What is the 'jest-environment-jsdom' Environment? 

The `jest-environment-jsdom` environment is a special environment that Jest uses to run tests in a browser-like environment. This environment provides a number of features, such as a DOM API, a way to simulate user interactions, and the ability to run asynchronous code. 

## What Causes the 'jest-environment-jsdom' Not Found Error?

The `jest-environment-jsdom` not found error can be caused by a few different issues. The most common causes are: 

1. The `jest-environment-jsdom` package is not installed. 
2. The `jest-environment-jsdom` package is installed, but the `testEnvironment` option in the Jest configuration is not set to `jsdom`. 
3. The `jest-environment-jsdom` package is installed, but the `testEnvironment` option in the Jest configuration is set to an incorrect value. 

## How to Troubleshoot the 'jest-environment-jsdom' Not Found Error

If you encounter the `jest-environment-jsdom` not found error, the first step is to check if the `jest-environment-jsdom` package is installed. To do this, you can run the following command in the terminal: 

```bash
$ npm list jest-environment-jsdom
```

If the `jest-environment-jsdom` package is installed, you should see it in the output of the command. 

If the `jest-environment-jsdom` package is installed, the next step is to check the `testEnvironment` option in the Jest configuration. This option should be set to `jsdom` in order for Jest to use the `jest-environment-jsdom` environment. To check the `testEnvironment` option, open the `package.json` file and look for the `jest` section. In this section, you should see a `testEnvironment` option. If it is set to `jsdom`, then the error is likely caused by an incorrect value. 

If the `testEnvironment` option is set to an incorrect value, you can change it to `jsdom` and re-run the tests. 

If the `jest-environment-jsdom` package is not installed, you can install it by running the following command in the terminal: 

```bash
$ npm install --save-dev jest-environment-jsdom
```

Once the package is installed, you should set the `testEnvironment` option in the Jest configuration to `jsdom` and re-run the tests. 

## Conclusion

The `jest-environment-jsdom` not found error can be caused by a few different issues. The most common causes are: the `jest-environment-jsdom` package is not installed, the `testEnvironment` option in the Jest configuration is not set to `jsdom`, or the `testEnvironment` option is set to an incorrect value. To troubleshoot this error, you should first check if the `jest-environment-jsdom` package is installed, and then check the `testEnvironment` option in the Jest configuration. If the package is not installed, you can install it, and if the `testEnvironment` option is set to an incorrect value, you can change it to `jsdom` and re-run the tests.

Are you getting an error when trying to run your Jest tests? If so, you may have encountered the `jest-environment-jsdom` not found error. In this blog post, we'll go over the steps you need to take to resolve this issue.

## What is Jest?

Jest is a popular JavaScript testing framework developed by Facebook. It is used to test React and other JavaScript applications. It's fast and has a lot of features that make it easy to use.

## What is the jest-environment-jsdom Error?

When running Jest tests, you may encounter an error that says `jest-environment-jsdom` not found. This error indicates that Jest is not able to find the jest-environment-jsdom module, which is required for running Jest tests.

## How to Fix the jest-environment-jsdom Error

To fix the jest-environment-jsdom error, you'll need to install the jest-environment-jsdom module. Here's how to do it:

1. Open your terminal and navigate to the root of your project.
2. Run the command `npm install --save-dev jest-environment-jsdom`.
3. Add the following code to your `package.json` file:

```json
"jest": {
  "testEnvironment": "jest-environment-jsdom"
}
```

4. Run the command `npm install` to install the jest-environment-jsdom module.

Once you've completed these steps, you should be able to run your Jest tests without any errors.

## Conclusion

The jest-environment-jsdom error can be a frustrating issue to deal with, but it's not too difficult to fix. By following the steps outlined in this blog post, you should be able to get your Jest tests running without any problems. Good luck!
## Recommended sites
- [Jest Test Environment Not Found](https://www.codementor.io/@dmitrymakhnev/jest-test-environment-not-found-5v5t9hf3y)
- [Testing with Jest: Test Environment Not Found](https://medium.com/@abhijithvijayan/testing-with-jest-test-environment-not-found-735e5f5f5f5a)
- [Jest Test Environment Not Found: A Troubleshooting Guide](https://blog.bitsrc.io/jest-test-environment-not-found-a-troubleshooting-guide-8a6f8e6c3a1e)
- [Jest Test Environment Not Found Error](https://www.thepolyglotdeveloper.com/2019/11/jest-test-environment-not-found-error/)