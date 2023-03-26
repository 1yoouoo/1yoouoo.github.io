---
layout: post
title: "Angular TypeError: Cannot Read Property 'onDestroy'"
tags: ['angular', 'typescript', 'modularization']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

The Angular TypeError: Cannot Read Property 'onDestroy' is an error that can occur when a user attempts to use the `onDestroy` method of a component. This error typically occurs when a user attempts to use the `onDestroy` method on a component that does not have one. This error can be a bit confusing for developers as the `onDestroy` method is a common method used in Angular applications. 

The `onDestroy` method is a life cycle hook that is part of the Angular framework. This method is called when a component is destroyed and is used to perform any necessary cleanup. It is important to note that not all components have an `onDestroy` method. This is because some components do not need to perform any cleanup when they are destroyed. 

A common mistake that leads to the Angular TypeError: Cannot Read Property 'onDestroy' is attempting to use the `onDestroy` method on a component that does not have one. In order to avoid this error, it is important to check the documentation to make sure the component has an `onDestroy` method before attempting to use it.

Another mistake that can lead to the Angular TypeError: Cannot Read Property 'onDestroy' is attempting to use the `onDestroy` method in a component that does not have a life cycle hook. In order to use the `onDestroy` method, the component must have a life cycle hook. If the component does not have a life cycle hook, then the `onDestroy` method cannot be used. 

Below is an example of code that will lead to the Angular TypeError: Cannot Read Property 'onDestroy':

```typescript
@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent {
  // Component code
 
  ngOnDestroy() {
    // Cleanup code
  }
}
```

In the example above, the `ngOnDestroy` method is used in the `ExampleComponent` class. This is an example of correct usage of the `onDestroy` method as the `ExampleComponent` class has a life cycle hook. 

If we were to attempt to use the `onDestroy` method in a component that does not have a life cycle hook, it would lead to the Angular TypeError: Cannot Read Property 'onDestroy'. Below is an example of code that will lead to the error:

```typescript
@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent {
  // Component code
 
  onDestroy() {
    // Cleanup code
  }
}
```

In the example above, the `onDestroy` method is used in the `ExampleComponent` class. This is an example of incorrect usage of the `onDestroy` method as the `ExampleComponent` class does not have a life cycle hook. 

It is important to remember that the `onDestroy` method is only available in components that have a life cycle hook. Attempting to use the `onDestroy` method in a component that does not have a life cycle hook will lead to the Angular TypeError: Cannot Read Property 'onDestroy'. It is also important to remember that not all components have an `onDestroy` method, so it is important to check the documentation before attempting to use the `onDestroy` method.

If you're a developer using Angular, you know the frustration of dealing with errors. One of the most common errors you may encounter is the TypeError: Cannot Read Property 'onDestroy'. This error usually occurs when the component you are trying to use has been destroyed. In this blog post, we'll look at what this error is and how to fix it.

## What is the TypeError: Cannot Read Property 'onDestroy' Error?

The TypeError: Cannot Read Property 'onDestroy' error is an Angular error that occurs when you try to access a property or method of a component that has been destroyed. This error is usually caused when the component has been destroyed, either by calling the `ngOnDestroy()` method or by removing the component from the DOM.

## How to Fix the TypeError: Cannot Read Property 'onDestroy' Error

The first step to fixing this error is to determine why the component was destroyed in the first place. If the component was removed from the DOM, it may be because the user has navigated away from the page or the component has been removed programmatically.

If the component was destroyed by calling the `ngOnDestroy()` method, it may be because the component is no longer needed or the user has navigated away from the page.

Once you have determined why the component was destroyed, you can take the appropriate action to fix the error.

### Case 1: Component Removed From DOM

If the component was removed from the DOM, you can simply add the component back to the DOM. This can be done using the `ViewContainerRef` class in Angular.

```typescript
import { ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-my-component',
  templateUrl: './my-component.component.html',
  styleUrls: ['./my-component.component.css']
})
export class MyComponentComponent {

  constructor(private viewContainerRef: ViewContainerRef) { }

  public showComponent() {
    this.viewContainerRef.createComponent(MyComponent);
  }

}
```

In the above code, we are using the `ViewContainerRef` class to create an instance of the component and add it to the DOM. This will ensure that the component is not destroyed and the error will be resolved.

### Case 2: Component Destroyed by Calling `ngOnDestroy()`

If the component was destroyed by calling the `ngOnDestroy()` method, you can simply remove the call to the method. This will ensure that the component is not destroyed and the error will be resolved.

```typescript
import { Component, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-my-component',
  templateUrl: './my-component.component.html',
  styleUrls: ['./my-component.component.css']
})
export class MyComponentComponent implements OnDestroy {

  ngOnDestroy() {
    // remove this line
  }

}
```

In the above code, we are removing the call to the `ngOnDestroy()` method. This will ensure that the component is not destroyed and the error will be resolved.

## Conclusion

The TypeError: Cannot Read Property 'onDestroy' error is a common error that can occur when you try to access a property or method of a component that has been destroyed. This error can be fixed by determining why the component was destroyed and taking the appropriate action. In most cases, this will involve either adding the component back to the DOM or removing the call to the `ngOnDestroy()` method. By following the steps outlined in this blog post, you should be able to successfully resolve this error.