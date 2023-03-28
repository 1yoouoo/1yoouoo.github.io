---
layout: post
title: "Troubleshooting ReferenceError: structuredClone is Not Defined with Jest and Node.js & Typescript"
tags: ['node.js', 'typescript', 'jestjs', 'ts-jest', 'structured-clone']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

If you are a developer working with Jest and Node.js & Typescript, you may have encountered a ReferenceError: structuredClone is not defined error. This error is typically encountered when running tests with Jest, and it can be difficult to troubleshoot. In this article, we will discuss what this error is, why it occurs, and how to fix it.

## What is ReferenceError: structuredClone is not defined?

ReferenceError: structuredClone is not defined is an error that occurs when running tests with Jest. It occurs when Jest attempts to clone an object, but the object does not have a structuredClone method. This can happen when trying to clone objects that are not supported by the structuredClone algorithm, such as Maps, Sets, and WeakMaps.

## Why does ReferenceError: structuredClone is not defined occur?

ReferenceError: structuredClone is not defined occurs when Jest attempts to clone an object, but the object does not have a structuredClone method. This can happen when trying to clone objects that are not supported by the structuredClone algorithm, such as Maps, Sets, and WeakMaps.

## How to fix ReferenceError: structuredClone is not defined

The best way to fix ReferenceError: structuredClone is not defined is to avoid trying to clone objects that are not supported by the structuredClone algorithm. If you need to clone an unsupported object, you can use a polyfill or a custom cloning function.

### Polyfill

A polyfill is a piece of code that implements a feature on web browsers that do not support it natively. To use a polyfill to clone an unsupported object, you can use the `structuredClone` polyfill from the `structured-clone` library.

```javascript
const structuredClone = require('structured-clone');

const clonedObject = structuredClone(unsupportedObject);
```

### Custom Cloning Function

If you don't want to use a polyfill, you can also create a custom cloning function. This function should create a shallow copy of the object and should be used in place of the `structuredClone` method.

```typescript
function customClone(obj: any): any {
  const clonedObj = {};
  for (const key in obj) {
    clonedObj[key] = obj[key];
  }
  return clonedObj;
}

const clonedObject = customClone(unsupportedObject);
```

## Conclusion

In this article, we discussed the ReferenceError: structuredClone is not defined error and how to fix it. We discussed why this error occurs and how to avoid it. Finally, we discussed two methods for cloning unsupported objects: using a polyfill or creating a custom cloning function.

If you encounter the `ReferenceError: structuredClone is not defined` error when running Jest and Node.js & Typescript, then you have come to the right place. This error is a common issue and can be quite difficult to troubleshoot and resolve. In this blog post, we will explain what this error is, why it occurs, and provide a step-by-step solution to fix it.

## What is the ReferenceError: structuredClone is Not Defined Error?

The `ReferenceError: structuredClone is not defined` error is a runtime error that occurs when running Jest and Node.js & Typescript. It is usually caused by a lack of the `structuredClone` API, which is used to create a deep clone of an object. Without this API, Jest and Node.js & Typescript will not be able to properly clone an object, resulting in the `ReferenceError: structuredClone is not defined` error.

## Why Does the ReferenceError: structuredClone is Not Defined Error Occur?

The `ReferenceError: structuredClone is not defined` error occurs when the `structuredClone` API is not available. This API is used to create a deep clone of an object, and is required for Jest and Node.js & Typescript to properly clone an object. Without this API, Jest and Node.js & Typescript will not be able to properly clone an object, resulting in the `ReferenceError: structuredClone is not defined` error.

## How to Fix the ReferenceError: structuredClone is Not Defined Error

To resolve the `ReferenceError: structuredClone is not defined` error, you must first ensure that the `structuredClone` API is available. This API is provided by the `node-structured-clone` package, which can be installed using `npm`:

```
npm install node-structured-clone
```

Once the `node-structured-clone` package is installed, you must then import the `structuredClone` API into your project. This can be done using the following code:

```javascript
import { structuredClone } from 'node-structured-clone';
```

Finally, you must then use the `structuredClone` API to clone the object that is causing the error. This can be done using the following code:

```javascript
const clonedObject = structuredClone(object);
```

Once you have imported the `structuredClone` API and used it to clone the object, the `ReferenceError: structuredClone is not defined` error should be resolved.

## Conclusion

In conclusion, the `ReferenceError: structuredClone is not defined` error is a common issue that occurs when running Jest and Node.js & Typescript. It is usually caused by a lack of the `structuredClone` API, which is used to create a deep clone of an object. To resolve this error, you must first ensure that the `node-structured-clone` package is installed, then import the `structuredClone` API into your project, and finally use the `structuredClone` API to clone the object that is causing the error. Following these steps should help you resolve the `ReferenceError: structuredClone is not defined` error.