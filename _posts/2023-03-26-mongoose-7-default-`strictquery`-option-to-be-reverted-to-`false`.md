---
layout: post
title: "Mongoose 7: Default `strictQuery` Option to be Reverted to `false`"
tags: ['javascript', 'node.js', 'mongodb', 'mongoose', 'deprecation-warning']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

Mongoose 7 is an object data modeling library for MongoDB and Node.js. It provides a straight-forward, schema-based solution to model your application data. It includes built-in type casting, validation, query building, business logic hooks and more, out of the box.

Recently, Mongoose 7 has been released with a new default setting for the `strictQuery` option. This option is used to determine whether Mongoose will throw an error when an unknown query key is specified. The new default setting is `false`, meaning that Mongoose will no longer throw an error when an unknown query key is specified.

This change has caused some confusion and frustration among developers, as it can lead to unexpected results. This article will explain the changes and the potential issues that can arise from them.

## What is the `strictQuery` Option?

The `strictQuery` option is a Mongoose setting that determines whether Mongoose will throw an error when an unknown query key is specified. It is enabled by default, meaning that Mongoose will throw an error when an unknown query key is specified.

For example, let's say you have a Mongoose model called `User` with the following schema:

```javascript
const UserSchema = new mongoose.Schema({
  name: String,
  age: Number
});
```

If you try to query the `User` model using an unknown key, such as `height`, Mongoose will throw an error:

```javascript
User.find({ height: '6ft' }) // Mongoose will throw an error
```

This is because Mongoose is designed to prevent you from querying fields that do not exist in the schema.

## Why the Change to `strictQuery`?

The default behavior of Mongoose is to throw an error when an unknown query key is specified. However, this can be inconvenient in some cases. For example, if you are using a third-party API that returns data in a format that is not compatible with your Mongoose schema, you may need to query using unknown keys.

In order to make it easier to query with unknown keys, Mongoose 7 has changed the default setting for the `strictQuery` option to `false`. This means that Mongoose will no longer throw an error when an unknown query key is specified.

## Potential Issues with the Change

While the change to the `strictQuery` option can be convenient in some cases, it can also lead to unexpected results. For example, if you are querying a model with an unknown key, you may get back results that you did not expect.

For example, let's say you have a `User` model with the following schema:

```javascript
const UserSchema = new mongoose.Schema({
  name: String,
  age: Number
});
```

If you query the `User` model using an unknown key, such as `height`, Mongoose will not throw an error. Instead, it will return all users, regardless of their height:

```javascript
User.find({ height: '6ft' }) // Mongoose will not throw an error
```

This can lead to unexpected results, as you may get back results that you did not expect.

## How to Avoid Unexpected Results

In order to avoid unexpected results when using the `strictQuery` option, it is important to always check the query keys before executing the query. This can be done by using the `validateQuery` method, which will throw an error if an unknown query key is specified.

For example, let's say you have a `User` model with the following schema:

```javascript
const UserSchema = new mongoose.Schema({
  name: String,
  age: Number
});
```

If you want to query the `User` model using an unknown key, such as `height`, you should first validate the query using the `validateQuery` method:

```javascript
User.validateQuery({ height: '6ft' }) // Mongoose will throw an error
```

This will throw an error if an unknown query key is specified, and prevent you from getting unexpected results.

## Conclusion

The change to the `strictQuery` option in Mongoose 7 can be convenient in some cases, but it can also lead to unexpected results. In order to avoid unexpected results, it is important to always check the query keys before executing the query. This can be done by using the `validateQuery` method, which will throw an error if an unknown query key is specified.

Mongoose 7 has introduced a new default setting for the `strictQuery` option, which is now set to `true` by default. This change has caused a lot of confusion and frustration for developers who were not expecting this change, as it can cause unexpected errors when performing queries. In this blog post, we will discuss what `strictQuery` is, why it was changed to `true`, and how you can revert it back to `false` if you need to.

## What is `strictQuery`?

`strictQuery` is a Mongoose option that was introduced in Mongoose 5. It is used to control how Mongoose handles queries. When `strictQuery` is set to `true`, Mongoose will throw an error if the query contains any fields that are not defined in the model. This is to prevent developers from accidentally querying fields that are not part of the model and returning incorrect results.

## Why was `strictQuery` changed to `true`?

The main reason why `strictQuery` was changed to `true` is to improve the security of Mongoose applications. By ensuring that all queries are limited to fields that are defined in the model, it reduces the risk of attackers being able to access data that is not intended for them.

## How can I revert `strictQuery` to `false`?

If you need to revert `strictQuery` to `false`, you can do so by setting it in the `mongoose.connect()` call. For example, if you are using the default Mongoose connection, you can set `strictQuery` to `false` like this:

```javascript
mongoose.connect(url, { useNewUrlParser: true, strictQuery: false });
```

Alternatively, you can also set `strictQuery` to `false` on a per-model basis. To do this, you will need to add the option to the `schema` object when you define the model. For example:

```javascript
const UserSchema = new mongoose.Schema({
    name: String,
    age: Number
}, { strictQuery: false });

const User = mongoose.model('User', UserSchema);
```

## Conclusion

In this blog post, we have discussed the new `strictQuery` option in Mongoose 7, why it was changed to `true` by default, and how you can revert it back to `false` if you need to. We hope that this has helped to clear up any confusion or frustration that developers may have encountered when using Mongoose 7.