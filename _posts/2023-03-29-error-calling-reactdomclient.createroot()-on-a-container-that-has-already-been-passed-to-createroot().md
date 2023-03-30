---
layout: post
title: "Error Calling ReactDOMClient.createRoot() on a Container That Has Already Been Passed to createRoot()"
tags: ['reactjs', 'react-18']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

ReactDOMClient.createRoot() is an API call used to create a React root container for a given component. It is used to render a React application into a container, such as a div, and mount it into the DOM. However, if a container has already been passed to ReactDOMClient.createRoot(), an error will be thrown. 

This error occurs when a container has already been passed to ReactDOMClient.createRoot(), meaning that a React root container has already been created for the given component. The error message will be "Error: Invariant Violation: ReactDOMClient.createRoot(): A React root container has already been created for this component."

A common mistake that leads to this error is attempting to call ReactDOMClient.createRoot() on a component that has already been mounted. This is because ReactDOMClient.createRoot() should only be called once per component. If a component has already been mounted, ReactDOMClient.createRoot() should not be called again.

Another common mistake is attempting to mount a component into the same container twice. This is because ReactDOMClient.createRoot() creates a React root container for the given component, and this container should only be used once. If the same container is used for two different components, an error will be thrown.

In order to avoid this error, it is important to ensure that ReactDOMClient.createRoot() is only called once per component. Additionally, it is important to ensure that each component is mounted into a unique container.

The following code snippet demonstrates how to avoid this error:

```javascript
// Create a div element to use as a container for our component
const container = document.createElement('div');

// Mount our component into the container
ReactDOMClient.createRoot(container).render(<MyComponent />);

// Attempting to call ReactDOMClient.createRoot() again will throw an error
ReactDOMClient.createRoot(container).render(<MyOtherComponent />); // Error: Invariant Violation: ReactDOMClient.createRoot(): A React root container has already been created for this component.
```

In this example, we create a div element to use as a container for our component. We then call ReactDOMClient.createRoot() on the container, passing in our component to mount. If we attempt to call ReactDOMClient.createRoot() again on the same container, an error will be thrown.

To avoid this error, it is important to ensure that ReactDOMClient.createRoot() is only called once per component. Additionally, it is important to ensure that each component is mounted into a unique container.

This error occurs when you attempt to call `ReactDOMClient.createRoot()` on a container that has already been passed to the same function. To understand the cause of the error and how to resolve it, let's first look at what `ReactDOMClient.createRoot()` does.

## What is ReactDOMClient.createRoot()?

`ReactDOMClient.createRoot()` is a method used to mount a React application to a DOM element. It is used to render a React component tree into a DOM element and manage its lifecycle. The first argument of the method is a DOM element, and the second argument is an optional object containing options for the root instance.

## What Causes the Error?

The error occurs when you attempt to call `ReactDOMClient.createRoot()` on a container that has already been passed to the same function. This is because `ReactDOMClient.createRoot()` is not designed to work on a container that has already been passed to it. 

When this error occurs, the `ReactDOMClient.createRoot()` call will fail and the application will not be mounted to the DOM element.

## How to Resolve the Error

To resolve this error, you must ensure that `ReactDOMClient.createRoot()` is only called once on a given container. This can be done in two ways:

### 1. Use a Unique Container

The simplest way to resolve this error is to use a unique container for each call to `ReactDOMClient.createRoot()`. This means that each call to `ReactDOMClient.createRoot()` should be made on a different DOM element.

For example, if you are calling `ReactDOMClient.createRoot()` multiple times, you can create a unique container for each call:

```javascript
const container1 = document.createElement('div');
const container2 = document.createElement('div');

ReactDOMClient.createRoot(container1, {});
ReactDOMClient.createRoot(container2, {});
```

### 2. Unmount the Container Before Calling ReactDOMClient.createRoot()

Alternatively, you can unmount the container before calling `ReactDOMClient.createRoot()`. This can be done using the `ReactDOMClient.unmountComponentAtNode()` method.

For example, if you are calling `ReactDOMClient.createRoot()` multiple times, you can unmount the container before each call:

```javascript
const container = document.createElement('div');

ReactDOMClient.createRoot(container, {});

// Unmount the container before calling ReactDOMClient.createRoot() again
ReactDOMClient.unmountComponentAtNode(container);

ReactDOMClient.createRoot(container, {});
```

## Conclusion

The error "Error Calling ReactDOMClient.createRoot() on a Container That Has Already Been Passed to createRoot()" occurs when you attempt to call `ReactDOMClient.createRoot()` on a container that has already been passed to the same function. To resolve this error, you must ensure that `ReactDOMClient.createRoot()` is only called once on a given container. This can be done by using a unique container for each call, or by unmounting the container before each call.
## Recommended sites

- [React - Error Calling ReactDOMClient.createRoot() on a Container That Has Already Been Passed to createRoot()](https://reactjs.org/docs/error-calling-reactdomclient-create-root-container.html)
- [Solving ReactDOMClient.createRoot() on a Container That Has Already Been Passed to createRoot()](https://www.codementor.io/@sahilpandita/solving-reactdomclient-create-root-container-that-has-already-been-passed-to-createroot-o8b6kf1y7)
- [Error Calling ReactDOMClient.createRoot() on a Container That Has Already Been Passed to createRoot()](https://stackoverflow.com/questions/54716482/error-calling-reactdomclient-create-root-on-a-container-that-has-already-been-pas)