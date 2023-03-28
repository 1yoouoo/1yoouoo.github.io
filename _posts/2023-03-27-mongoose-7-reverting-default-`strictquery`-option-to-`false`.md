---
layout: post
title: Mongoose 7: Reverting Default `strictQuery` Option to `false`
tags: ['javascript', 'node.js', 'mongodb', 'mongoose', 'deprecation-warning']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When Mongoose 7 was released, one of the changes that caused confusion among developers was the revert of the default `strictQuery` option to `false`. This change has implications for how Mongoose handles queries, and it's important to understand what it means and how it affects your code.

## What is the `strictQuery` Option?

The `strictQuery` option is a setting that determines how Mongoose handles queries. When `strictQuery` is set to `true`, Mongoose will throw an error if you try to query a field that is not defined in your schema. This is useful for ensuring that you don't accidentally query fields that don't exist in your database.

## Why Was the Default Changed from `true` to `false`?

The default for `strictQuery` was changed from `true` to `false` to make it easier for developers to query fields that are not defined in their schema. This makes it easier to query fields that are not explicitly defined in the schema, such as fields that are added by plugins or fields that are added by other developers working on the same project.

## What Does the Change Mean for My Code?

The change from `true` to `false` means that Mongoose will no longer throw an error if you try to query a field that is not defined in your schema. This means that you can query fields that are not explicitly defined in the schema, such as fields that are added by plugins or fields that are added by other developers working on the same project.

However, it's important to note that setting `strictQuery` to `false` does not mean that Mongoose will automatically add fields to your schema. If you query a field that is not defined in your schema, Mongoose will just ignore it and not return any results.

## What Are Some Common Mistakes to Avoid?

When using the `strictQuery` option, it's important to remember that setting it to `false` does not mean that Mongoose will automatically add fields to your schema. If you query a field that is not defined in your schema, Mongoose will just ignore it and not return any results.

Another common mistake is to forget to set the `strictQuery` option to `true` when necessary. If you're working on a project where you need to ensure that all queries are valid, then you should set `strictQuery` to `true`. This will ensure that Mongoose throws an error if you try to query a field that is not defined in your schema.

## Conclusion

Understanding Mongoose 7's revert of the default `strictQuery` option to `false` is important for understanding how Mongoose handles queries. Setting `strictQuery` to `false` means that Mongoose will no longer throw an error if you try to query a field that is not defined in your schema, but it does not mean that Mongoose will automatically add fields to your schema. It's important to remember to set `strictQuery` to `true` when necessary, and to remember that Mongoose will just ignore fields that are not defined in the schema if `strictQuery` is set to `false`.
Mongoose is a popular Object Document Mapper (ODM) that allows developers to interact with MongoDB databases using JavaScript. In Mongoose 7, the default `strictQuery` option has been reverted to `false`, meaning that query parameters are no longer required to be explicitly declared in the schema. This change can cause unexpected errors if you are not aware of it.

## What is `strictQuery`?
The `strictQuery` option is used to determine how Mongoose handles query parameters that are not explicitly declared in the schema. When set to `true`, Mongoose will throw an error if any unknown query parameters are provided. When set to `false`, Mongoose will ignore any unknown query parameters.

## Why was the Default Reverted to `false`?
The default value of `strictQuery` was changed from `true` to `false` in order to make Mongoose more user-friendly. By reverting the default to `false`, Mongoose will no longer throw an error if a query parameter is not explicitly declared in the schema. This makes it easier for developers to quickly get up and running with Mongoose without having to worry about declaring all of their query parameters in the schema.

## What are the Potential Issues?
The potential issue with reverting the default value of `strictQuery` to `false` is that it can lead to unexpected behavior if you are not aware of the change. Without strictQuery enabled, Mongoose will ignore any unknown query parameters that are provided, which could lead to incorrect results or unexpected behavior.

## How to Resolve the Issue
The easiest way to resolve this issue is to explicitly set the `strictQuery` option to `true` in your schema. This will ensure that Mongoose will throw an error if any unknown query parameters are provided.

For example, if you have a `User` model with the following schema:

```javascript
const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
});
```

You can set the `strictQuery` option to `true` like so:

```javascript
const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, required: true },
}, {
  strictQuery: true,
});
```

Now, if an unknown query parameter is provided, Mongoose will throw an error.

## Conclusion
Reverting the default `strictQuery` option to `false` in Mongoose 7 can lead to unexpected behavior if you are not aware of the change. To ensure that Mongoose is handling query parameters correctly, it is recommended that you explicitly set the `strictQuery` option to `true` in your schema. This will ensure that Mongoose will throw an error if any unknown query parameters are provided.