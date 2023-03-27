---
layout: post
title: "Modifying DTO Name in NestJS OpenAPI (Swagger) Schemas"
tags: ['swagger', 'nestjs', 'schema', 'openapi', 'dto']
---

![Image of a Cat](http://source.unsplash.com/1600x900/?cat)
When setting up an OpenAPI (Swagger) Schema in NestJS, it is important to note that the name of the Data Transfer Object (DTO) used to define the request body must match the name of the property in the schema. Otherwise, the schema will not be set up correctly and the application will throw an error. This article will explain the importance of this requirement, as well as provide examples of how to properly set up a NestJS OpenAPI (Swagger) Schema.

## Why is the DTO Name Important?
The DTO name is important in NestJS OpenAPI (Swagger) Schemas because it is used to define the request body. Without a properly named DTO, the request body will not be set up correctly, and the application will throw an error. This error is usually a **TypeError**, and it occurs when the DTO name does not match the name of the property in the schema. 

For example, if the DTO name is `UserDTO`, but the property in the schema is `user`, the error will look like this:

```
TypeError: Cannot read property 'user' of undefined
```

This error occurs because the DTO name does not match the property in the schema, so the application is unable to read the property. 

## How to Properly Set Up a NestJS OpenAPI (Swagger) Schema
In order to properly set up a NestJS OpenAPI (Swagger) Schema, the DTO name must match the property in the schema. To do this, the DTO must be defined within the `@Controller` decorator of the controller, and the `@ApiBody` decorator must be used to define the request body.

For example, if the property in the schema is `user`, the DTO should be defined as follows:

```typescript
@Controller('users')
export class UsersController {
  @Post()
  @ApiBody({ type: UserDTO })
  async createUser(@Body() user: UserDTO) {
    // Create user
  }
}
```

In this example, the DTO is defined as `UserDTO`, and the `@ApiBody` decorator is used to define the request body. This ensures that the DTO name matches the property in the schema, and that the application will be able to read the property correctly.

## Conclusion
In conclusion, it is important to remember that the DTO name must match the property in the schema when setting up an OpenAPI (Swagger) Schema in NestJS. If the DTO name does not match the property in the schema, the application will throw an error. To properly set up a NestJS OpenAPI (Swagger) Schema, the DTO must be defined within the `@Controller` decorator of the controller, and the `@ApiBody` decorator must be used to define the request body.
When developing APIs with NestJS, the OpenAPI (Swagger) schemas are automatically generated based on the decorators and classes we define. However, when we want to modify the name of a Data Transfer Object (DTO) in the OpenAPI schema, we can run into issues. In this blog post, we will discuss how to modify the DTO name in NestJS OpenAPI (Swagger) schemas.

## What is a DTO?
A Data Transfer Object (DTO) is a type of object used to transfer data between different components or services. DTOs are generally used to transfer data from the backend to the frontend, or from the frontend to the backend. They are often used in web services, such as REST APIs, to transfer data between the server and the client.

## What is OpenAPI (Swagger)?
OpenAPI (Swagger) is an open-source framework for creating and documenting APIs. It provides a way to describe the structure of an API, including its endpoints, operations, and parameters. It also provides a way to generate client libraries and server stubs for different programming languages.

## Modifying the DTO Name in NestJS OpenAPI (Swagger) Schemas
NestJS provides a way to generate OpenAPI (Swagger) schemas from the code we write. By default, the DTO name in the OpenAPI schema is the same as the name of the DTO class. However, if we want to change the DTO name in the OpenAPI schema, we can use the `@ApiProperty()` decorator.

The `@ApiProperty()` decorator is used to add additional information to the OpenAPI schema. It takes two parameters: the name of the property and an optional description. We can use this decorator to change the name of the DTO in the OpenAPI schema.

For example, let's say we have a DTO class called `UserDto`:

```typescript
export class UserDto {
  @ApiProperty()
  id: number;

  @ApiProperty()
  name: string;
}
```

By default, the name of this DTO in the OpenAPI schema would be `UserDto`. To change the name of the DTO in the OpenAPI schema, we can use the `@ApiProperty()` decorator:

```typescript
export class UserDto {
  @ApiProperty({ name: 'user_id' })
  id: number;

  @ApiProperty({ name: 'user_name' })
  name: string;
}
```

Now, the name of the DTO in the OpenAPI schema will be `user_id` and `user_name` respectively.

## Conclusion
In this blog post, we discussed how to modify the DTO name in NestJS OpenAPI (Swagger) schemas. We learned that we can use the `@ApiProperty()` decorator to change the name of the DTO in the OpenAPI schema. We also saw an example of how to use the `@ApiProperty()` decorator to change the name of a DTO. We hope this blog post has been helpful in understanding how to modify the DTO name in NestJS OpenAPI (Swagger) schemas.