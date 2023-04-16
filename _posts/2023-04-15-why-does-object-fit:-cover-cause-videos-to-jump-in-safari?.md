---
layout: post
title: "Why Does Object-Fit: Cover Cause Videos to Jump in Safari?"
tags: ['html', 'css', 'safari', 'object-fit']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)
Object-Fit: Cover is a CSS property used to crop an element to fit within a certain area of the page. This property is commonly used to make sure that images, videos, and other elements fit within a container without being distorted or cut off. However, when used with videos, this property can cause unexpected behavior in Safari, causing the video to jump or flicker when the page is scrolled. In this article, we'll explore why this happens and how to fix it.

## What is Object-Fit: Cover?
Object-Fit: Cover is a CSS property that is used to resize an element to fit within a certain area. This property can be applied to images, videos, and other elements to ensure that they fit within the container without being distorted or cut off.

## What Causes Videos to Jump in Safari?
When Object-Fit: Cover is used with videos in Safari, the video can jump or flicker when the page is scrolled. This issue is caused by the way Safari handles the Object-Fit: Cover property. 

When Object-Fit: Cover is applied to a video, Safari creates a copy of the video in memory and then applies the property to it. This means that when the page is scrolled, the video must be re-rendered, which causes the video to jump or flicker.

## How to Fix the Issue
The best way to fix this issue is to use the `object-fit: contain` property instead of `object-fit: cover`. This property does not create a copy of the video in memory, so it does not cause the video to jump or flicker when the page is scrolled.

```css
video {
    object-fit: contain;
}
```

In addition to using `object-fit: contain`, you can also use the `object-position` property to adjust the position of the video within the container.

```css
video {
    object-fit: contain;
    object-position: center;
}
```

## Common Mistakes
When using Object-Fit: Cover with videos, it is important to remember that this property can cause unexpected behavior in Safari. To avoid this issue, it is best to use the `object-fit: contain` property instead. Additionally, it is important to remember to use the `object-position` property to adjust the position of the video within the container.
If you’ve ever tried using the `object-fit: cover` CSS property to make a video or image take up the full width of a page in Safari, you may have noticed that the video or image will jump or move around when the page is scrolled. This can be incredibly frustrating, especially if you’ve spent a lot of time getting the styling just right.

In this blog post, we’ll explore why this happens, and what you can do to fix it. We’ll look at a few examples of how to use `object-fit: cover` correctly, and how to avoid the jumping issue.

## What is Object-Fit: Cover?
`Object-fit: cover` is a CSS property that allows you to control how an element is sized and positioned within its parent container. It is most commonly used to make images and videos take up the full width of a page, regardless of the size of their parent container.

## Why Does Object-Fit: Cover Cause Videos to Jump in Safari?
The issue with `object-fit: cover` in Safari is due to a bug in the browser’s rendering engine. The bug causes the video or image to jump around when the page is scrolled, as if the element is being repositioned.

The bug is caused by Safari’s handling of the `overflow` property. When an element has `overflow: hidden`, Safari will incorrectly apply the `object-fit: cover` property to the element, causing it to jump around when the page is scrolled.

## How to Fix the Issue
Fortunately, there are a few ways to fix this issue. The first is to simply not use `overflow: hidden` on the parent container. If you need the parent container to be hidden, you can use `overflow: visible` instead.

The second way to fix the issue is to wrap the video or image element in a `div` with `overflow: hidden`, and then apply the `object-fit: cover` property to the `div` instead. This will ensure that the element is not affected by the bug.

## Examples of Object-Fit: Cover
Let’s look at a few examples of how to use `object-fit: cover` correctly.

### Example 1
In this example, we have a `div` with an image inside. We want the image to take up the full width of the parent container, so we set the `object-fit: cover` property on the image.

```html
<div>
  <img src="example.jpg" style="object-fit: cover; width: 100%; height: 100%;" />
</div>
```

### Example 2
In this example, we have a `div` with a video inside. We want the video to take up the full width of the parent container, so we set the `object-fit: cover` property on the video.

```html
<div>
  <video src="example.mp4" style="object-fit: cover; width: 100%; height: 100%;" />
</div>
```

### Example 3
In this example, we have a `div` with an image inside. We want the image to take up the full width of the parent container, but we also want to hide the overflow. To do this, we wrap the image in a `div` with `overflow: hidden` and set the `object-fit: cover` property on the `div`.

```html
<div style="overflow: hidden;">
  <div style="object-fit: cover; width: 100%; height: 100%;">
    <img src="example.jpg" />
  </div>
</div>
```

## Conclusion
By understanding why `object-fit: cover` causes videos to jump in Safari, and how to fix the issue, you can ensure that your videos and images look great on all browsers.

If you need to use `overflow: hidden` on the parent container, simply wrap the element in a `div` and apply the `object-fit: cover` property to the `div` instead. This will ensure that the element is not affected by the bug.

We hope this blog post has been helpful in understanding why `object-fit: cover` causes videos to jump in Safari, and how to fix the issue.
## Recommended Sites
[Why Does Object-Fit: Cover Cause Videos to Jump in Safari?](https://css-tricks.com/why-does-object-fit-cover-cause-videos-to-jump-in-safari/)

[What is the object-fit property in CSS?](https://www.quora.com/What-is-the-object-fit-property-in-CSS)

[object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)