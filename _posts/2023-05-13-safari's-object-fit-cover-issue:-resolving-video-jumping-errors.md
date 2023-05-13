---
layout: post
title: "Safari's Object-fit Cover Issue: Resolving Video Jumping Errors"
tags: ['html', 'css', 'safari', 'object-fit']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

## Understanding the Issue

Safari's object-fit cover issue is a common problem faced by developers when working with videos on the web. This issue occurs when a video element with the CSS property `object-fit: cover` is used in Safari, causing the video to jump or flicker during playback. In this article, we will delve into the causes of this issue and explore potential solutions.

### Common Mistakes and Reasons for Errors

1. **Lack of Browser Compatibility**: The `object-fit` property is not supported by all browsers, especially older versions of Safari. Therefore, it is essential to check browser compatibility before using this property.

2. **Incorrect Usage of CSS Properties**: Sometimes, developers might misuse the `object-fit` property or use it in conjunction with other CSS properties that conflict with it, causing the video jumping error.

### Delving into the Code

To better understand the issue, let's consider an example where the video jumping error occurs. Here's a sample HTML structure with a video element:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Test</title>
    <style>
        .video-container {
            position: relative;
            width: 100%;
            height: 0;
            padding-bottom: 56.25%;
            overflow: hidden;
        }

        video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <div class="video-container">
        <video src="path/to/video.mp4" autoplay loop muted></video>
    </div>
</body>
</html>
```

In this example, the video element has been assigned the CSS property `object-fit: cover`. This property ensures that the video maintains its aspect ratio while filling the container's entire width and height. However, in Safari, this causes the video to jump or flicker during playback.

### A Potential Solution: Using JavaScript

One way to resolve this issue is by using JavaScript to dynamically adjust the video's dimensions based on the container's aspect ratio. Here's an example of how this can be done:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const video = document.querySelector('video');
    const container = document.querySelector('.video-container');

    function resizeVideo() {
        const containerAspectRatio = container.offsetWidth / container.offsetHeight;
        const videoAspectRatio = video.videoWidth / video.videoHeight;

        if (containerAspectRatio > videoAspectRatio) {
            video.style.width = '100%';
            video.style.height = 'auto';
        } else {
            video.style.width = 'auto';
            video.style.height = '100%';
        }
    }

    video.addEventListener('loadedmetadata', resizeVideo);
    window.addEventListener('resize', resizeVideo);
});
```

In this code snippet, we first select the video and its container. Then, we create a function called `resizeVideo` that calculates the aspect ratios of both the container and the video. Based on these aspect ratios, the function adjusts the video's width and height accordingly. This function is then called when the video's metadata is loaded and whenever the window is resized.

### Testing the Solution

To test this solution, replace the `object-fit: cover` property in the original example's CSS with the following:

```css
video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
}
```

Then, add the JavaScript code snippet provided above to the HTML file. This should resolve the video jumping issue in Safari while maintaining the desired behavior in other browsers.

### Further Considerations

While this solution addresses the video jumping error, it may not be suitable for all use cases. For instance, if the video must be centered within the container, additional JavaScript code might be required to calculate and apply the necessary offsets.

### Exploring Alternative Solutions

Another approach to resolving the video jumping issue is to use CSS `background-size: cover` instead of `object-fit: cover`. This method involves setting the video as a background of a container element and using the `background-size` property to achieve the desired behavior. However, this solution has its limitations, as it requires additional work to handle video controls and accessibility features.

In conclusion, Safari's object-fit cover issue can be a frustrating problem for developers working with videos on the web. By understanding the underlying causes and exploring potential solutions, you can ensure a smooth and seamless video playback experience for your users across all browsers.

However, there is a specific issue that arises when using the `object-fit: cover;` property in Safari, which causes video elements to "jump" or "skip" when they are resized. This can be a frustrating error for developers, as it affects the overall user experience and can make a website look unprofessional. In this blog post, we will dive deep into this error and provide a step-by-step solution to resolve it.

**Step 1: Identify the issue**

Before we can solve the problem, it's important to understand what's causing it. The issue occurs when using the `object-fit: cover;` property on a video element in Safari. This property tells the browser to scale the video so that it covers the entire container, while maintaining its aspect ratio. Unfortunately, Safari seems to have some trouble handling this property correctly, causing the video to jump or skip when it's resized.

**Step 2: Create a test case**

To demonstrate this issue, let's create a simple HTML file with a video element and some basic CSS styling. Here's an example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Object-fit Cover Issue</title>
  <style>
    .video-container {
      width: 100%;
      height: 100vh;
      overflow: hidden;
      position: relative;
    }

    video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      position: absolute;
    }
  </style>
</head>
<body>
  <div class="video-container">
    <video autoplay muted loop>
      <source src="path/to/your/video.mp4" type="video/mp4">
    </video>
  </div>
</body>
</html>
```

In this example, we have a full-screen video container with a video element inside it. The `object-fit: cover;` property is applied to the video element, which should cause it to scale appropriately and cover the entire container.

**Step 3: Observe the issue in Safari**

Open the test case in Safari and resize the browser window. You should notice that the video jumps or skips as the window is resized. This is the error we are trying to fix.

**Step 4: Implement a workaround**

Since the issue seems to be specific to Safari's handling of the `object-fit: cover;` property, one way to resolve it is by using JavaScript to detect the browser and apply a workaround for Safari only. We can do this using the `navigator.userAgent` property, which returns a string containing information about the user's browser.

Here's an example of how to implement this workaround:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  const isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);

  if (isSafari) {
    const video = document.querySelector('video');
    video.addEventListener('loadedmetadata', function() {
      const aspectRatio = video.videoWidth / video.videoHeight;
      const containerAspectRatio = video.parentElement.offsetWidth / video.parentElement.offsetHeight;

      if (aspectRatio > containerAspectRatio) {
        video.style.width = '100%';
        video.style.height = 'auto';
      } else {
        video.style.width = 'auto';
        video.style.height = '100%';
      }
    });
  }
});
```

In this example, we first check if the user's browser is Safari by testing the `navigator.userAgent` string against a regular expression. If the browser is Safari, we then add an event listener to the video element that listens for the `loadedmetadata` event. This event is fired when the video's metadata (such as dimensions and duration) has been loaded.

Inside the event handler, we calculate the aspect ratio of the video and its container, and then update the video's width and height accordingly. This effectively achieves the same result as using `object-fit: cover;`, but without the jumping or skipping issue.

**Step 5: Test the workaround**

Now that we've implemented the workaround, open the test case in Safari again and resize the browser window. The video should no longer jump or skip, and it should still maintain its aspect ratio while covering the entire container.

In conclusion, the `object-fit: cover;` property is a powerful tool for creating responsive designs, but it can cause issues in some browsers, like Safari. By implementing the workaround described in this blog post, you can ensure that your videos look great and function smoothly across all browsers. Remember to always test your designs in multiple browsers to catch and resolve any potential issues.
# Recommended Sites

1. [Apple Developer Documentation: object-fit](https://developer.apple.com/documentation/webkitjs/css_style_declaration/1631693-object-fit)
2. [MDN Web Docs: object-fit](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
3. [CSS-Tricks: Using CSS object-fit for Videos](https://css-tricks.com/using-css-object-fit-for-videos/)
4. [Stack Overflow: Safari Object-fit CSS Issue](https://stackoverflow.com/questions/38068367/safari-object-fit-css-issue)
5. [WebKit Bugzilla: object-fit: cover not working on video](https://bugs.webkit.org/show_bug.cgi?id=153856)