// Test file for basic case conversions
import {
  toUpperCase,
  toLowerCase,
  toCamelCase,
  toPascalCase,
  toSnakeCase,
  toKebabCase,
  toTitleCase,
  toSentenceCase,
  toDotCase,
  toSpaceCase,
  toFlatCase,
  toHttpHeaderCase,
  toCamelSnakeCase,
  toHungarianCase,
  toMacroCase,
  toPascalSnakeCase,
  toPathCase,
  toSlashTitleCase,
} from '../index.js';

export default function runBasicTests() {
  describe('Basic Case Conversions', () => {
  test('toUpperCase', () => {
    expect(toUpperCase('hello world')).toBe('HELLO WORLD');
    expect(toUpperCase('test case')).toBe('TEST CASE');
  });

  test('toLowerCase', () => {
    expect(toLowerCase('HELLO WORLD')).toBe('hello world');
    expect(toLowerCase('Test Case')).toBe('test case');
  });

  test('toCamelCase', () => {
    expect(toCamelCase('hello world')).toBe('helloWorld');
    expect(toCamelCase('test-case')).toBe('testCase');
    expect(toCamelCase('snake_case')).toBe('snakeCase');
    expect(toCamelCase('PascalCase')).toBe('pascalCase');
  });

  test('toPascalCase', () => {
    expect(toPascalCase('hello world')).toBe('HelloWorld');
    expect(toPascalCase('test-case')).toBe('TestCase');
    expect(toPascalCase('snake_case')).toBe('SnakeCase');
    expect(toPascalCase('camelCase')).toBe('CamelCase');
  });

  test('toSnakeCase', () => {
    expect(toSnakeCase('hello world')).toBe('hello_world');
    expect(toSnakeCase('testCase')).toBe('test_case');
    expect(toSnakeCase('PascalCase')).toBe('pascal_case');
    expect(toSnakeCase('kebab-case')).toBe('kebab_case');
  });

  test('toKebabCase', () => {
    expect(toKebabCase('hello world')).toBe('hello-world');
    expect(toKebabCase('testCase')).toBe('test-case');
    expect(toKebabCase('PascalCase')).toBe('pascal-case');
    expect(toKebabCase('snake_case')).toBe('snake-case');
  });

  test('toTitleCase', () => {
    expect(toTitleCase('hello world')).toBe('Hello World');
    expect(toTitleCase('test case')).toBe('Test Case');
    expect(toTitleCase('snake_case')).toBe('Snake_Case');
  });

  test('toSentenceCase', () => {
    expect(toSentenceCase('hello world')).toBe('Hello world');
    expect(toSentenceCase('test case')).toBe('Test case');
    expect(toSentenceCase('SNAKE_CASE')).toBe('Snake_case');
  });

  test('toDotCase', () => {
    expect(toDotCase('hello world')).toBe('hello.world');
    expect(toDotCase('test case')).toBe('test.case');
    expect(toDotCase('snake_case')).toBe('snake.case');
  });

  test('toSpaceCase', () => {
    expect(toSpaceCase('hello_world')).toBe('hello world');
    expect(toSpaceCase('test-case')).toBe('test case');
    expect(toSpaceCase('camelCase')).toBe('camel case');
  });

  test('toFlatCase', () => {
    expect(toFlatCase('hello world')).toBe('helloworld');
    expect(toFlatCase('test-case')).toBe('testcase');
    expect(toFlatCase('snake_case')).toBe('snakecase');
  });

  test('toHttpHeaderCase', () => {
    expect(toHttpHeaderCase('content-type')).toBe('Content-Type');
    expect(toHttpHeaderCase('user-agent')).toBe('User-Agent');
    expect(toHttpHeaderCase('accept-encoding')).toBe('Accept-Encoding');
  });

  test('toCamelSnakeCase', () => {
    expect(toCamelSnakeCase('hello world')).toBe('hello_world');
    expect(toCamelSnakeCase('testCase')).toBe('test_case');
    expect(toCamelSnakeCase('PascalCase')).toBe('pascal_case');
  });

  test('toHungarianCase', () => {
    expect(toHungarianCase('strUserName')).toBe('strUserName');
    expect(toHungarianCase('iCount')).toBe('iCount');
    expect(toHungarianCase('bIsAdmin')).toBe('bIsAdmin');
    expect(toHungarianCase('hello world')).toBe('helloWorld');
  });

  test('toMacroCase', () => {
    expect(toMacroCase('hello world')).toBe('HELLO_WORLD');
    expect(toMacroCase('test case')).toBe('TEST_CASE');
    expect(toMacroCase('snake_case')).toBe('SNAKE_CASE');
  });

  test('toPascalSnakeCase', () => {
    expect(toPascalSnakeCase('hello world')).toBe('Hello_World');
    expect(toPascalSnakeCase('test case')).toBe('Test_Case');
    expect(toPascalSnakeCase('snake_case')).toBe('Snake_Case');
  });

  test('toPathCase', () => {
    expect(toPathCase('api/users')).toBe('api/users');
    expect(toPathCase('api/v1/users')).toBe('api/v1/users');
    expect(toPathCase('hello/world')).toBe('hello/world');
  });

  test('toSlashTitleCase', () => {
    expect(toSlashTitleCase('hello/world')).toBe('Hello/World');
    expect(toSlashTitleCase('api/users')).toBe('Api/Users');
    expect(toSlashTitleCase('test/case')).toBe('Test/Case');
  });
  });
}
