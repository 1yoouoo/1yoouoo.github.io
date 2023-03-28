---
layout: post
title: "Mongoose 7: Default `strictQuery` Option to be Switched Back to `false`"
tags: ['javascript', 'node.js', 'mongodb', 'mongoose', 'deprecation-warning']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Mongoose 7 has introduced a new default option for the `strictQuery` option, which is now set to `true` by default. This change can cause unexpected errors when querying data in Mongoose, as the `strictQuery` option is used to control whether Mongoose will automatically add properties to the query that are not specified.

It is important to understand why this change was made and how it can affect your queries. In this article, we will explore the `strictQuery` option and how it can affect your queries. We will also look at some common mistakes that can occur when using the `strictQuery` option, as well as how to avoid them.

## What is the `strictQuery` Option?

The `strictQuery` option is a Mongoose option that is used to control whether Mongoose will automatically add properties to the query that are not specified. This option is set to `true` by default in Mongoose 7, which means that Mongoose will not add any additional properties to the query.

If you want Mongoose to add additional properties to the query, you will need to explicitly set the `strictQuery` option to `false`. This can be done by passing the `strictQuery` option as an argument when creating a new Mongoose instance.

```javascript
const mongoose = new Mongoose({
    strictQuery: false
});
```

When the `strictQuery` option is set to `false`, Mongoose will add any additional properties to the query that are not specified. This can be useful for some queries, as it can allow you to query for data that is not explicitly specified in the query.

## Common Mistakes with the `strictQuery` Option

When using the `strictQuery` option, it is important to understand the implications of setting it to `true` or `false`. Setting the `strictQuery` option to `false` can be useful for some queries, but it can also lead to unexpected results if you are not careful.

One of the most common mistakes when using the `strictQuery` option is not understanding the implications of setting it to `false`. When the `strictQuery` option is set to `false`, Mongoose will add any additional properties to the query that are not specified. This can lead to unexpected results, as Mongoose will add properties that you may not have intended to include in the query.

Another common mistake is not understanding the implications of setting the `strictQuery` option to `true`. When the `strictQuery` option is set to `true`, Mongoose will not add any additional properties to the query. This can lead to errors if you are trying to query for data that is not explicitly specified in the query.

## Conclusion

In this article, we explored the `strictQuery` option in Mongoose 7 and how it can affect your queries. We looked at some common mistakes that can occur when using the `strictQuery` option, as well as how to avoid them. By understanding the implications of setting the `strictQuery` option to `true` or `false`, you can ensure that your queries are as accurate as possible.

Mongoose 7 introduced a new `strictQuery` option that is set to `true` by default. This option can cause unexpected errors when querying documents in a MongoDB database. In this blog post, we'll discuss why this option was introduced, what it does, and how to switch it back to `false` to avoid unexpected errors.

## What is the `strictQuery` Option?

The `strictQuery` option is a new feature introduced in Mongoose 7 that restricts the fields that can be queried in a MongoDB database. It is set to `true` by default, which means that if you attempt to query a field that is not defined in your Mongoose schema, an error will be thrown.

For example, let's say we have a `User` model with the following schema:

```javascript
const UserSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  age: {
    type: Number,
    required: true
  }
});
```

If we try to query a field that is not defined in the schema (e.g. `address`), an error will be thrown:

```
MongooseError: The `address` path is not in the schema and strictQuery is set to `true`.
```

## Why was the `strictQuery` Option Introduced?

The `strictQuery` option was introduced in Mongoose 7 to provide an extra layer of security when querying documents in a MongoDB database. By default, it prevents developers from querying fields that are not defined in the schema, which can help prevent malicious users from accessing sensitive data.

## How to Switch the `strictQuery` Option Back to `false`

If you are getting unexpected errors when querying documents in a MongoDB database, you may need to switch the `strictQuery` option back to `false`. To do this, you can set the `strictQuery` option to `false` when creating your Mongoose model:

```javascript
const User = mongoose.model('User', UserSchema, { strictQuery: false });
```

Alternatively, you can also set the `strictQuery` option to `false` when creating your Mongoose connection:

```javascript
const connection = mongoose.createConnection(uri, { strictQuery: false });
```

## Conclusion

The `strictQuery` option is a new feature introduced in Mongoose 7 that restricts the fields that can be queried in a MongoDB database. It is set to `true` by default, which can cause unexpected errors when querying documents in a MongoDB database. If you are getting unexpected errors when querying documents in a MongoDB database, you may need to switch the `strictQuery` option back to `false`. To do this, you can set the `strictQuery` option to `false` when creating your Mongoose model or connection.