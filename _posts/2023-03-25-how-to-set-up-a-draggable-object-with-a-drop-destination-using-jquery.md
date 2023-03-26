---
layout: post
title: "How to Set Up a Draggable Object with a Drop Destination Using jQuery"
tags: ['javascript', 'html', 'jquery', 'css']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

With jQuery, developers can create draggable objects and drop destinations to create a user-friendly interface. This tutorial will walk through the steps to create a draggable object with a drop destination using jQuery.

## Setting Up the HTML

The first step is to set up the HTML. The draggable object and the drop destination will both be `div` elements. The draggable object will have the class `draggable` and the drop destination will have the class `droppable`.

```html
<div class="draggable">Drag Me!</div>
<div class="droppable"></div>
```

## Adding the jQuery

The next step is to add jQuery to the page. This can be done by including the jQuery library from a CDN or by downloading the library and adding it to the page.

## Making the Object Draggable

Once the HTML and jQuery are set up, the draggable object can be made draggable using the `draggable()` method. This method takes an object as an argument and can be used to set options for the draggable object.

```javascript
$('.draggable').draggable({
    containment: 'parent',
    revert: 'invalid'
});
```

The `containment` option is used to restrict the draggable object within the parent element. This is helpful when the draggable object is larger than the drop destination. The `revert` option is used to set the behavior of the draggable object when it is not dropped on a valid drop destination. In this example, the object will move back to its original position if it is not dropped on a valid drop destination.

## Making the Drop Destination

Making the drop destination is done using the `droppable()` method. This method takes an object as an argument and can be used to set options for the drop destination.

```javascript
$('.droppable').droppable({
    accept: '.draggable',
    drop: function(event, ui) {
        $(this).append(ui.draggable);
    }
});
```

The `accept` option is used to specify which draggable objects can be dropped on the drop destination. In this example, only elements with the class `draggable` can be dropped on the drop destination. The `drop` option is used to set the behavior when a draggable object is dropped on the drop destination. In this example, the draggable object is appended to the drop destination when it is dropped.

## Testing

Once the HTML, jQuery, and draggable/droppable settings are set up, the draggable object can be tested. The draggable object should be able to be dragged around the page and dropped on the drop destination. When the draggable object is dropped on the drop destination, it should be appended to the drop destination.

## Common Mistakes

When setting up a draggable object with a drop destination using jQuery, there are a few common mistakes to look out for. One common mistake is forgetting to set the `containment` option for the draggable object. Without setting this option, the draggable object can be dragged outside of the parent element. Another common mistake is forgetting to set the `accept` option for the drop destination. Without setting this option, any draggable object can be dropped on the drop destination.

The ability to drag and drop elements on a webpage is a powerful tool for web developers. It allows for more complex user interactions, and can help create a more engaging user experience. jQuery makes it very easy to implement drag and drop functionality, and this tutorial will walk you through the process of setting up a draggable object with a drop destination.

## Step 1: Include jQuery

The first step is to include jQuery in your project. You can either download the library from the jQuery website, or you can use a CDN. To use a CDN, simply add the following line of code to the `<head>` section of your HTML document:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
```

## Step 2: Set Up the HTML

Next, we need to set up the HTML for the draggable object and the drop destination. For this example, we'll use two `<div>` elements. The first will be the draggable object, and the second will be the drop destination.

```html
<div class="draggable">
    Drag me!
</div>

<div class="drop-destination">
    Drop here
</div>
```

## Step 3: Add CSS Styles

Now we need to add some CSS styles to make the elements look the way we want. For this example, we'll give the draggable object a background color and a border, and we'll give the drop destination a border as well.

```css
.draggable {
    background-color: #ccc;
    border: 1px solid #000;
    padding: 10px;
}

.drop-destination {
    border: 1px dashed #000;
    padding: 10px;
}
```

## Step 4: Add jQuery

Now we need to add the jQuery code to make the elements draggable and droppable. We'll start by selecting the draggable element and making it draggable.

```javascript
$('.draggable').draggable();
```

Next, we'll select the drop destination and make it droppable.

```javascript
$('.drop-destination').droppable({
    drop: function(event, ui) {
        // code to run when an element is dropped
    }
});
```

The `drop` option specifies a function to be called when an element is dropped on the drop destination. This function can be used to perform any necessary tasks, such as updating data or displaying a message.

## Step 5: Test It Out

Now that we have our code set up, let's test it out. Open up your browser and you should be able to drag the draggable element and drop it on the drop destination. When you do, the function specified in the `drop` option should be called.

## Conclusion

In this tutorial, we learned how to set up a draggable object with a drop destination using jQuery. We included jQuery, set up the HTML, added some CSS styles, and added the jQuery code to make the elements draggable and droppable. Finally, we tested it out and saw that it worked. With this knowledge, you should be able to easily add drag and drop functionality to your own projects.