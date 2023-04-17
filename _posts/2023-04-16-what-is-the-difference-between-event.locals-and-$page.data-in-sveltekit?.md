---
layout: post
title: "What is the Difference Between Event.locals and $page.data in Sveltekit?"
tags: ['typescript', 'svelte', 'sveltekit']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

The Sveltekit framework is an exciting new development tool that allows developers to quickly create web applications. It uses a component-based architecture and provides an easy-to-use API for creating components and managing their state. One of the features of Sveltekit is the ability to access data from the page context. This data is stored in two different variables, Event.locals and $page.data. In this article, we will explore the differences between these two variables and how they can be used to access page data.

## What is Event.locals?

Event.locals is a variable that is available in the page context of Sveltekit. It is used to store data that is specific to the current page. This data can be accessed from the page's components and is available in the page's lifecycle hooks.

Event.locals is a plain JavaScript object, and it can store any kind of data. This makes it a very useful tool for passing data between components, as well as storing data that needs to be accessed throughout the page's lifecycle.

## What is $page.data?

$page.data is a special variable that is available in the page context of Sveltekit. It is used to store data that is shared across all pages in the application. This data can be accessed from any component in the application, regardless of its location in the page hierarchy.

Unlike Event.locals, $page.data is not a plain JavaScript object. It is a special object that is managed by Sveltekit. This means that it is not possible to directly modify the data stored in $page.data. Instead, it must be updated using the setPageData() method, which takes a key and a value as parameters.

## What is the Difference Between Event.locals and $page.data?

The main difference between Event.locals and $page.data is the scope of the data that they store. Event.locals stores data that is specific to the current page, while $page.data stores data that is shared across all pages in the application.

Another difference between the two variables is how they are managed. Event.locals is a plain JavaScript object, and it can be directly modified using standard JavaScript methods. $page.data, on the other hand, is a special object that is managed by Sveltekit, and it can only be modified using the setPageData() method.

## Common Mistakes

When using Event.locals and $page.data, it is important to remember the differences between the two variables. One common mistake is to try and directly modify the data stored in $page.data. As mentioned above, this is not possible, and any changes must be made using the setPageData() method.

Another common mistake is to try and use Event.locals to store data that needs to be shared across multiple pages. Event.locals is only available in the page context, and any data stored in it will not be available in other pages. For this reason, it is important to use $page.data for any data that needs to be shared across multiple pages.

## Conclusion

In this article, we have explored the differences between Event.locals and $page.data in Sveltekit. Event.locals is a plain JavaScript object that stores data that is specific to the current page, while $page.data is a special object that stores data that is shared across all pages in the application. It is important to remember the differences between these two variables when working with page data in Sveltekit.

When developing a Sveltekit application, you might encounter an error related to the `Event.locals` and `$page.data` variables. This error can be confusing, but understanding the differences between these two variables can help you resolve it quickly.

In Sveltekit, `Event.locals` and `$page.data` are used to store data that is passed between components. Both variables are objects and can be used to store any data type, including strings, numbers, arrays, and objects. The main difference between `Event.locals` and `$page.data` is how they are used.

## Event.locals

`Event.locals` is used to pass data between components in a Sveltekit application. It works by attaching data to an event, which is then passed to the component that is listening for the event. For example, if you wanted to pass a string from one component to another, you could use `Event.locals` to do so.

```javascript
// Component A
<button on:click={() => {
    const data = 'Hello World!';
    this.dispatch('my-event', { data });
}}>Click Me</button>

// Component B
<script>
    import { onMount } from 'svelte';

    let data;

    onMount(() => {
        this.on('my-event', ({ detail }) => {
            data = detail.data;
        });
    });
</script>

<p>{data}</p>
```

In this example, the `data` variable is attached to the `my-event` event and is passed to Component B when the button is clicked. The `onMount` function is used to listen for the event, and the `detail` property of the event is used to access the data.

## $page.data

`$page.data` is used to store data that is shared between components in a Sveltekit application. Unlike `Event.locals`, `$page.data` is not attached to an event, so it can be accessed from any component. For example, if you wanted to store a string that could be accessed from multiple components, you could use `$page.data` to do so.

```javascript
// Component A
<script>
    import { set } from 'svelte';

    set($page, 'data', 'Hello World!');
</script>

// Component B
<script>
    import { get } from 'svelte';

    let data = get($page, 'data');
</script>

<p>{data}</p>
```

In this example, the `data` variable is set in Component A and is accessed in Component B using the `get` function. This allows the data to be shared between components.

## Conclusion

Understanding the differences between `Event.locals` and `$page.data` can help you resolve any errors related to these variables. `Event.locals` is used to pass data between components, while `$page.data` is used to store data that is shared between components. When used correctly, these variables can be a powerful tool for managing data in a Sveltekit application.
## Recommended Sites

- [What is the Difference Between Event.locals and $page.data in Sveltekit?](https://www.thewebdev.dev/difference-between-event-locals-and-page-data-in-sveltekit/)
- [SvelteKit - Event.locals and $page.data](https://svelte.dev/tutorial/event-locals-and-page-data)
- [SvelteKit - Event.locals and $page.data](https://www.sitepoint.com/sveltekit-event-locals-and-page-data/)
- [What is the Difference Between Event.locals and $page.data in Sveltekit?](https://www.techiediaries.com/sveltekit-event-locals-page-data/)