---
layout: post
title: "TypeError: Property 'session' Does Not Exist on Type '{}'"
tags: ['reactjs', 'typescript', 'next.js', 'next-auth']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When writing code in Typescript or Javascript, it is important to understand the different types of errors that can be encountered. One of the most common errors is the TypeError, which is thrown when a property is accessed on a type that doesn't support it. In this article, we will discuss the TypeError: Property 'session' Does Not Exist on Type '{}' and some of the common mistakes that can lead to this error.

## What is TypeError: Property 'session' Does Not Exist on Type '{}'?

The TypeError: Property 'session' Does Not Exist on Type '{}' is an error that is thrown when a property is accessed on a type that does not support it. In other words, the code is trying to access a property that does not exist on the type. This is a common error when working with objects and classes, as the code may be trying to access a property that does not exist on the object or class.

For example, consider the following code:

```typescript
let myObject = {};
let mySession = myObject.session;
```

In this code, we are trying to access the `session` property on the `myObject` object. However, this object does not have a `session` property, so the code will throw a TypeError: Property 'session' Does Not Exist on Type '{}' error.

## Common Mistakes

When working with objects and classes, there are a few common mistakes that can lead to the TypeError: Property 'session' Does Not Exist on Type '{}' error.

The first mistake is trying to access a property that does not exist on the object or class. As we saw in the example above, this will throw a TypeError: Property 'session' Does Not Exist on Type '{}' error. It is important to always check the object or class to make sure that the property exists before attempting to access it.

The second mistake is trying to access a property on an object or class that is not of the correct type. For example, consider the following code:

```typescript
let myObject = {};
let mySession = myObject.session;
```

In this code, we are trying to access the `session` property on the `myObject` object. However, this object is not of type `Session`, so the code will throw a TypeError: Property 'session' Does Not Exist on Type '{}' error. It is important to make sure that the object or class is of the correct type before attempting to access the property.

The third mistake is forgetting to declare a property before attempting to access it. For example, consider the following code:

```typescript
let myObject = {};
let mySession = myObject.session;
```

In this code, we are trying to access the `session` property on the `myObject` object. However, this property has not been declared, so the code will throw a TypeError: Property 'session' Does Not Exist on Type '{}' error. It is important to always declare a property before attempting to access it.

## Conclusion

The TypeError: Property 'session' Does Not Exist on Type '{}' is an error that is thrown when a property is accessed on a type that does not support it. This error is typically caused by trying to access a property that does not exist on the object or class, trying to access a property on an object or class that is not of the correct type, or forgetting to declare a property before attempting to access it. It is important to understand these common mistakes in order to avoid this error.

This error is a common one in the world of programming, especially when dealing with TypeScript or JavaScript. It occurs when a variable, object, or array is declared and the code attempts to access a property or method that does not exist on the declared type. In this case, the error specifically states that the property 'session' does not exist on type '{}'. 

To understand this error, it is important to first understand the basics of types in TypeScript and JavaScript. Both TypeScript and JavaScript are strongly typed languages, meaning that each variable or object has a specific type. This type can be one of the primitive types (number, string, boolean, undefined, null, and symbol) or a more complex type like an object, array, or function.

When a variable, object, or array is declared, the type of that variable or object is set. This type cannot be changed, and any attempt to access a property or method that does not exist on that type will result in an error. In this case, the error is stating that the property 'session' does not exist on the type '{}'.

To resolve this error, it is important to first understand what type the variable or object is. If the type is an object, then the code must ensure that the property 'session' exists on the object. If the type is an array, then the code must ensure that the index of the array is valid. 

If the code is attempting to access a property or method that does not exist on the type, then the code must be changed to access a property or method that does exist. This can be done by either changing the type of the variable or object, or accessing a different property or method on the existing type.

Below is an example of code that will result in this error:

```javascript
const myObject = {};

myObject.session; // TypeError: Property 'session' does not exist on type '{}'
```

In this example, the variable `myObject` is declared as an object with the type `{}`. Since the object does not have a property called `session`, the code will throw an error when attempting to access the property. 

To resolve this error, the code must be changed to either access a different property or method on the object, or to change the type of the object. For example, if the code was expecting the object to have a property called `session`, then the code could be changed to the following:

```javascript
const myObject = {
  session: 'mySession'
};

myObject.session; // 'mySession'
```

In this example, the type of the object is changed to include the property `session`. The code can now successfully access the property without throwing an error.

In summary, the TypeError `Property 'session' does not exist on type '{}'` is a common error in TypeScript and JavaScript. It occurs when a variable, object, or array is declared and the code attempts to access a property or method that does not exist on the declared type. To resolve this error, the code must be changed to either access a different property or method on the object, or to change the type of the object.
## Recommended Sites
- [MDN Web Docs - TypeError: Property 'session' Does Not Exist on Type '{}'](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_does_not_exist_on_type)
- [Stack Overflow - TypeError: Property 'session' Does Not Exist on Type '{}'](https://stackoverflow.com/questions/59991772/typeerror-property-session-does-not-exist-on-type)
- [W3Schools - TypeError: Property 'session' Does Not Exist on Type '{}'](https://www.w3schools.com/js/js_errors.asp)