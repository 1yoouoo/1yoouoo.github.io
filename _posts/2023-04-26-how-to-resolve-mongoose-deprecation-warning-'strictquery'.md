---
layout: post
title: "How to Resolve Mongoose Deprecation Warning 'strictQuery' "
tags: ['node.js', 'mongodb', 'mongoose', 'deprecation-warning']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. It provides a straight-forward, schema-based solution to model your application data. Mongoose has become the most popular library for MongoDB in the Node.js world. Mongoose provides a layer of abstraction over MongoDB that makes it easier to work with MongoDB.

However, there are some Mongoose deprecation warnings that may appear when working with Mongoose. One such warning is the 'strictQuery' warning. This warning can appear when you are using the `findOneAndUpdate` or `findOneAndDelete` methods in Mongoose. These methods allow you to update or delete a document in the database without retrieving the document first.

The 'strictQuery' warning is a reminder that the query you are using is not using the strict mode. Strict mode ensures that the query you are using is valid and that the document you are trying to update or delete actually exists. Without strict mode, Mongoose will allow you to update or delete a document even if it does not exist.

To resolve the 'strictQuery' warning, you need to set the `strict` option to `true` when calling the `findOneAndUpdate` or `findOneAndDelete` methods. This will ensure that the query you are using is valid and that the document you are trying to update or delete actually exists.

```javascript
// Set the strict option to true when using findOneAndUpdate
User.findOneAndUpdate({name: 'John'}, {age: 30}, {strict: true}, function(err, user) {
  if (err) {
    // Handle error
  } else {
    // Handle success
  }
});

// Set the strict option to true when using findOneAndDelete
User.findOneAndDelete({name: 'John'}, {strict: true}, function(err, user) {
  if (err) {
    // Handle error
  } else {
    // Handle success
  }
});
```

Another common mistake is forgetting to set the `strict` option when using the `findOneAndReplace` method. This method also requires the `strict` option to be set to `true` in order to ensure that the query you are using is valid and that the document you are trying to replace actually exists.

```javascript
// Set the strict option to true when using findOneAndReplace
User.findOneAndReplace({name: 'John'}, {name: 'Jane'}, {strict: true}, function(err, user) {
  if (err) {
    // Handle error
  } else {
    // Handle success
  }
});
```

When using the `findOneAndReplace` method, it is also important to note that the `new` option must be set to `true` in order for the updated document to be returned. Without the `new` option set to `true`, the original document will be returned instead of the updated document.

```javascript
// Set the new option to true when using findOneAndReplace
User.findOneAndReplace({name: 'John'}, {name: 'Jane'}, {strict: true, new: true}, function(err, user) {
  if (err) {
    // Handle error
  } else {
    // Handle success
  }
});
```

Finally, it is important to note that the `strict` and `new` options are not available when using the `findOneAndDelete` method. This is because the `findOneAndDelete` method does not return the deleted document.

In conclusion, the 'strictQuery' warning is a reminder that the query you are using is not using the strict mode. To resolve the warning, you need to set the `strict` option to `true` when calling the `findOneAndUpdate`, `findOneAndReplace`, or `findOneAndDelete` methods. It is also important to note that the `new` option must be set to `true` when using the `findOneAndReplace` method. Finally, the `strict` and `new` options are not available when using the `findOneAndDelete` method.

Mongoose is a popular object modeling library for Node.js and MongoDB. Recently, the Mongoose team released version 5.x, which includes a new feature called `strictQuery` that enables stricter query validation. While this feature is useful for ensuring that queries are valid, it can also lead to some unexpected errors. In this blog post, we'll discuss what the `strictQuery` feature is, why it can cause errors, and how to resolve those errors.

## What is the 'strictQuery' Feature?

The `strictQuery` feature is a new Mongoose feature that was introduced in version 5.x. It enables Mongoose to validate queries, ensuring that they are valid before executing them. This can help to prevent errors caused by invalid queries, such as attempting to query for a field that doesn't exist.

## Why Can the 'strictQuery' Feature Cause Errors?

The `strictQuery` feature can cause errors because it is enabled by default in Mongoose 5.x. This means that any queries that are made with Mongoose 5.x will be validated, which can cause unexpected errors if the query is invalid.

## How to Resolve 'strictQuery' Errors

If you're getting unexpected errors due to the `strictQuery` feature, there are a few ways to resolve them. The most straightforward way is to disable the feature, which can be done by setting the `strictQuery` option to `false`. This can be done when creating a Mongoose instance, like so:

```javascript
const mongoose = require('mongoose');
const mongooseOptions = {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  strictQuery: false
};
mongoose.connect('mongodb://localhost/my-database', mongooseOptions);
```

Alternatively, you can disable the `strictQuery` feature for specific queries by passing the `strictQuery` option as a query option, like so:

```javascript
MyModel.find({
  name: 'John Doe'
}, {
  strictQuery: false
});
```

## Conclusion

The `strictQuery` feature in Mongoose 5.x can be useful for ensuring that queries are valid, but it can also lead to unexpected errors. To resolve these errors, you can either disable the feature completely, or disable it for specific queries. Hopefully this blog post has helped you understand how to resolve `strictQuery` errors in Mongoose.
## Recommended Sites
- [Mongoose: Deprecation Warnings](https://mongoosejs.com/docs/deprecations.html#-strictquery)
- [How to Resolve Mongoose Deprecation Warning 'strictQuery'](https://www.codementor.io/@jasoncarter/how-to-resolve-mongoose-deprecation-warning-strictquery-1lm5j8v5f)
- [Mongoose v5.9.4: Deprecations](https://mongoosejs.com/docs/deprecations.html)
- [Mongoose Deprecation Warnings: strictQuery](https://www.npmjs.com/package/mongoose-strict-query)