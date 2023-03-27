---
layout: post
title: "Using 'Component' as a JSX Component Causes Error TS2786"
tags: ['reactjs', 'typescript', 'react-dom', 'tsx']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When writing React applications, developers often rely on the JSX syntax to create components. Unfortunately, this can sometimes lead to errors, such as the infamous TS2786. This error is caused when a developer attempts to use the keyword `Component` as a component name in a JSX expression. Here, we will discuss this error in more detail, what causes it, and how to fix it.

## What is Error TS2786?

Error TS2786 is a type-checking error that occurs when a developer attempts to use the keyword `Component` as a component name in a JSX expression. This is because `Component` is a reserved word in TypeScript, and cannot be used as a component name.

## What Causes Error TS2786?

Error TS2786 is caused by attempting to use the keyword `Component` as a component name in a JSX expression. This is because `Component` is a reserved word in TypeScript, and cannot be used as a component name.

## How to Fix Error TS2786

The simplest way to fix Error TS2786 is to simply rename the component to something else. For example, if you were attempting to use the component `Component`, you could rename it to `MyComponent`, `MyApp`, or anything else that isn't a reserved keyword.

```javascript
// Before
function Component() {
  return <div>My Component</div>;
}

// After
function MyComponent() {
  return <div>My Component</div>;
}
```

Alternatively, you can also use the `as` keyword to alias the component name. This will allow you to use the same component name, but it will be aliased to a different name in the output code.

```javascript
function Component() {
  return <div>My Component</div>;
}

export default Component as MyComponent;
```

## Conclusion

Error TS2786 occurs when a developer attempts to use the keyword `Component` as a component name in a JSX expression. This is because `Component` is a reserved word in TypeScript, and cannot be used as a component name. To fix this error, simply rename the component to something else, or use the `as` keyword to alias the component name.

If you've been writing React code for a while, you'll likely have seen this error before. It's one of the most common errors when using React, and it can be quite frustrating to debug. In this blog post, we'll discuss the cause of this error, and how to fix it.

## What is Error TS2786?

Error TS2786 is a TypeScript error that occurs when you try to use the `Component` class as a JSX component. This error is caused by the fact that `Component` is a base class for React components, and it doesn't have the necessary methods for use as a JSX component.

In order to use `Component` as a JSX component, you must first extend it to create a class that implements the necessary methods.

## How to Fix this Error?

To fix this error, you must first create a class that extends `Component`. This class must implement the necessary methods for use as a JSX component.

For example, let's say we have a `MyComponent` class that extends `Component`:

```jsx
class MyComponent extends Component {
  // ...
}
```

In order to use `MyComponent` as a JSX component, we must implement the `render()` method. This method must return a valid JSX element:

```jsx
class MyComponent extends Component {
  render() {
    return <div>Hello, world!</div>;
  }
}
```

Now, we can use `MyComponent` as a JSX component:

```jsx
<MyComponent />
```

In addition to the `render()` method, you may also need to implement other methods, such as `componentDidMount()` and `componentDidUpdate()`, depending on your use case.

## Conclusion

Error TS2786 occurs when you try to use the `Component` class as a JSX component. To fix this error, you must create a class that extends `Component` and implements the necessary methods for use as a JSX component. This includes the `render()` method, as well as any other methods that may be necessary for your use case. Once you have implemented the required methods, you can use the class as a JSX component.