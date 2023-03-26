---
layout: post
title: "Error: Module 'typeorm' Has No Exported Members 'DataSource' and 'DataSourceOptions'
tags: ['node.js', 'npm', 'nestjs', 'typeorm']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)

When working with `TypeORM`, a popular Object-Relational Mapping (ORM) library used to interact with databases in JavaScript and TypeScript, you may encounter an error saying `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'`. This error is caused by incorrect usage of the `DataSource` and `DataSourceOptions` properties when defining a connection to a database. In this article, we will explore what this error means and how to solve it.

## What Does the Error Mean?

The `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error occurs when attempting to create a connection to a database using `TypeORM`. This error indicates that the `DataSource` and `DataSourceOptions` properties were not correctly specified in the connection configuration.

The `DataSource` property specifies the database type and the `DataSourceOptions` property specifies the database-specific options for connecting to the database. Both of these properties are required for creating a connection to the database.

## Common Mistakes

When working with `TypeORM`, it is easy to make mistakes that can lead to the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error. Here are some of the most common mistakes that can lead to this error:

1. **Not Specifying the DataSource Property**: The `DataSource` property is required for creating a connection to the database. If this property is not specified, the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error will occur.

2. **Incorrectly Specifying the DataSource Property**: The `DataSource` property must be specified correctly in order for the connection to be successful. If the `DataSource` property is specified incorrectly, the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error will occur.

## Example

In order to illustrate how to solve the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error, let's take a look at an example.

Here is an example of a connection configuration that will result in the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error:

```typescript
// This will result in an error
createConnection({
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'password'
});
```

As you can see, the `DataSource` and `DataSourceOptions` properties are not specified in the connection configuration. This will result in the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error.

To solve this error, we need to specify the `DataSource` and `DataSourceOptions` properties in the connection configuration. Here is an example of a correct connection configuration:

```typescript
// This will not result in an error
createConnection({
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'password',
  dataSource: 'postgres',
  dataSourceOptions: {
    database: 'my_database'
  }
});
```

As you can see, we have specified the `DataSource` and `DataSourceOptions` properties in the connection configuration. This will solve the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error.

## Conclusion

In this article, we explored what the `Module 'typeorm' has no exported members 'DataSource' and 'DataSourceOptions'` error means and how to solve it. We also looked at some common mistakes that can lead to this error and an example of a connection configuration that will solve it.

This error is encountered when trying to import the `DataSource` and `DataSourceOptions` modules from the `typeorm` package. This error occurs because the `typeorm` package does not export these modules.

## What Causes This Error?

This error is caused by the `typeorm` package not exporting the `DataSource` and `DataSourceOptions` modules. This means that when you try to import these modules, you will get an error.

## How to Fix This Error

The best way to fix this error is to use the `@types/typeorm` package instead of the `typeorm` package. This package contains the necessary type definitions for the `typeorm` package, which will allow you to import the `DataSource` and `DataSourceOptions` modules without getting an error.

To install the `@types/typeorm` package, run the following command in your terminal:

```bash
npm install --save-dev @types/typeorm
```

Once the package has been installed, you can import the `DataSource` and `DataSourceOptions` modules like so:

```typescript
import { DataSource, DataSourceOptions } from '@types/typeorm';
```

## Conclusion

In this article, we have discussed the error “Module 'typeorm' Has No Exported Members 'DataSource' and 'DataSourceOptions'” and how to fix it. We have seen that the best way to fix this error is to use the `@types/typeorm` package instead of the `typeorm` package. We have also seen how to install and use the `@types/typeorm` package to import the `DataSource` and `DataSourceOptions` modules without getting an error.