#!/usr/bin/env node

import {
  toCamelCase,
  toSnakeCase,
  toKebabCase,
  toPascalCase,
  toTitleCase,
  CamelCase,
  SnakeCase,
  KebabCase,
} from './index.js';

console.log('🎯 magic-case Examples\n');

// Function-based API
console.log('📝 Function-based API:');
console.log('  toCamelCase("hello world"):', toCamelCase('hello world'));
console.log('  toSnakeCase("camelCase"):', toSnakeCase('camelCase'));
console.log('  toKebabCase("PascalCase"):', toKebabCase('PascalCase'));
console.log('  toPascalCase("hello world"):', toPascalCase('hello world'));
console.log('  toTitleCase("hello world"):', toTitleCase('hello world'));

console.log('\n🏗️  Class-based API:');
const camel = new CamelCase('hello world');
console.log('  new CamelCase("hello world"):', camel.toString());

const snake = new SnakeCase('camelCase');
console.log('  new SnakeCase("camelCase"):', snake.toString());

const kebab = new KebabCase('PascalCase');
console.log('  new KebabCase("PascalCase"):', kebab.toString());

console.log('\n🔗 Chaining transformations:');
const chain1 = new SnakeCase(camel);
console.log('  new SnakeCase(camel):', chain1.toString());

const chain2 = new KebabCase(chain1);
console.log('  new KebabCase(chain1):', chain2.toString());

console.log('\n✨ All examples completed!');
