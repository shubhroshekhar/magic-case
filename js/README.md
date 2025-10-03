# magic-case ✨

A magical text case converter for JavaScript — lightweight, fast, and feature-rich! 🪄

Convert strings between 18+ different case styles with a simple, intuitive API.

## 🚀 Features

- 🔄 **18+ Case Styles** - Convert between camelCase, snake_case, kebab-case, and more
- 🖥️ **CLI Support** - Command-line tool for quick conversions
- 🌐 **Universal** - Works in Node.js, browsers, and Deno
- 📦 **Zero Dependencies** - Lightweight and fast
- 🧪 **Well Tested** - Comprehensive test suite
- 📚 **TypeScript Ready** - Full type definitions included
- 🎯 **Class-based API** - Object-oriented approach for complex transformations

## 📦 Installation

```bash
npm install magic-case
```

## 🎯 Quick Start

### Function-based API (Simple)

```javascript
import { toCamelCase, toSnakeCase, toKebabCase } from 'magic-case';

console.log(toCamelCase('hello world')); // helloWorld
console.log(toSnakeCase('camelCase')); // camel_case
console.log(toKebabCase('PascalCase')); // pascal-case
```

### Class-based API (Advanced)

```javascript
import { CamelCase, SnakeCase, KebabCase } from 'magic-case';

const camel = new CamelCase('hello world');
console.log(camel.toString()); // helloWorld

const snake = new SnakeCase('camelCase');
console.log(snake.toString()); // camel_case

// Chain transformations
const kebab = new KebabCase(snake);
console.log(kebab.toString()); // camel-case
```

## 🎨 Available Case Styles

| Style                 | Function              | Class             | Example        |
| --------------------- | --------------------- | ----------------- | -------------- |
| **UPPERCASE**         | `toUpperCase()`       | `UpperCase`       | `HELLO WORLD`  |
| **lowercase**         | `toLowerCase()`       | `LowerCase`       | `hello world`  |
| **camelCase**         | `toCamelCase()`       | `CamelCase`       | `helloWorld`   |
| **PascalCase**        | `toPascalCase()`      | `PascalCase`      | `HelloWorld`   |
| **snake_case**        | `toSnakeCase()`       | `SnakeCase`       | `hello_world`  |
| **kebab-case**        | `toKebabCase()`       | `KebabCase`       | `hello-world`  |
| **Title Case**        | `toTitleCase()`       | `TitleCase`       | `Hello World`  |
| **Sentence case**     | `toSentenceCase()`    | `SentenceCase`    | `Hello world`  |
| **dot.case**          | `toDotCase()`         | `DotCase`         | `hello.world`  |
| **space case**        | `toSpaceCase()`       | `SpaceCase`       | `hello world`  |
| **flatcase**          | `toFlatCase()`        | `FlatCase`        | `helloworld`   |
| **HTTP-Header-Case**  | `toHttpHeaderCase()`  | `HttpHeaderCase`  | `Content-Type` |
| **camel_snake_case**  | `toCamelSnakeCase()`  | `CamelSnakeCase`  | `hello_world`  |
| **HungarianCase**     | `toHungarianCase()`   | `HungarianCase`   | `strUserName`  |
| **MACRO_CASE**        | `toMacroCase()`       | `MacroCase`       | `HELLO_WORLD`  |
| **Pascal_Snake_Case** | `toPascalSnakeCase()` | `PascalSnakeCase` | `Hello_World`  |
| **path/case**         | `toPathCase()`        | `PathCase`        | `api/users`    |
| **Slash/Title/Case**  | `toSlashTitleCase()`  | `SlashTitleCase`  | `Hello/World`  |

## 🖥️ CLI Usage

Install globally for command-line access:

```bash
npm install -g magic-case
```

Then use it anywhere:

```bash
magic-case camel "hello world"        # helloWorld
magic-case snake "camelCase"          # camel_case
magic-case kebab "PascalCase"         # pascal-case
magic-case title "hello world"        # Hello World
```

### CLI Help

```bash
magic-case --help
```

## 📚 API Reference

### Function-based API

All functions accept a string and return the converted string:

```javascript
import { toCamelCase, toSnakeCase, toKebabCase } from 'magic-case';

// Basic usage
toCamelCase('hello world'); // 'helloWorld'
toSnakeCase('camelCase'); // 'camel_case'
toKebabCase('PascalCase'); // 'pascal-case'
```

### Class-based API

Classes provide more control and can be chained:

```javascript
import { CamelCase, SnakeCase, KebabCase } from 'magic-case';

// Create instances
const camel = new CamelCase('hello world');
const snake = new SnakeCase('camelCase');

// Convert to string
console.log(camel.toString()); // 'helloWorld'
console.log(snake.toString()); // 'camel_case'

// Chain transformations
const kebab = new KebabCase(snake);
console.log(kebab.toString()); // 'camel-case'

// Access words array
console.log(camel.words); // ['hello', 'world']
```

### Error Handling

Some case styles have validation rules:

```javascript
import { CamelCase, HttpHeaderCase } from 'magic-case';

// CamelCase must start with lowercase
try {
  new CamelCase('PascalCase'); // Throws error
} catch (error) {
  console.log(error.message); // "Invalid CamelCase: must start with a lowercase letter"
}

// HttpHeaderCase must match specific format
try {
  new HttpHeaderCase('invalid-header'); // Throws error
} catch (error) {
  console.log(error.message); // "Invalid HttpHeaderCase string"
}
```

## 🌐 Browser Usage

```html
<script type="module">
  import {
    toCamelCase,
    toSnakeCase,
  } from 'https://unpkg.com/magic-case@latest/index.js';

  console.log(toCamelCase('hello world')); // helloWorld
  console.log(toSnakeCase('camelCase')); // camel_case
</script>
```

## 🧪 Testing

Run the test suite:

```bash
npm test
```

## 🔧 Development

Clone the repository and install dependencies:

```bash
git clone https://github.com/shubhroshekhar/magic-case.git
cd magic-case/js
npm install
```

### Available Scripts

- `npm test` - Run tests
- `npm run build` - Build CommonJS version
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## 📊 Performance

magic-case is optimized for performance:

- **Zero dependencies** - No external libraries
- **Lightweight** - Minimal bundle size
- **Fast** - Optimized algorithms
- **Memory efficient** - No unnecessary allocations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

MIT License © 2025 Shubhro Shekhar

## 🔗 Links

- [GitHub Repository](https://github.com/shubhroshekhar/magic-case)
- [npm Package](https://www.npmjs.com/package/magic-case)
- [Python Version](https://pypi.org/project/magic-case/)

---

Made with ❤️ by [Shubhro Shekhar](https://github.com/shubhroshekhar)
