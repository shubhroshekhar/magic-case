// Test file for class-based case conversions
import {
  BaseCase,
  SnakeCase,
  CamelCase,
  PascalCase,
  KebabCase,
  UpperCase,
  LowerCase,
  SentenceCase,
  TitleCase,
  DotCase,
  SpaceCase,
  FlatCase,
  HttpHeaderCase,
  CamelSnakeCase,
  HungarianCase,
  MacroCase,
  PascalSnakeCase,
  PathCase,
  SlashTitleCase,
} from '../index.js';

export default function runClassTests() {
  describe('Class-based Case Conversions', () => {
    test('BaseCase functionality', () => {
      const snake = new SnakeCase('hello world');
      expect(snake.words).toEqual(['hello_world']);
      expect(snake.toString()).toBe('hello_world');
      expect(snake.get()).toBe('hello_world');

      // Test BaseCase with another BaseCase instance
      const camel = new CamelCase(snake);
      expect(camel.toString()).toBe('helloWorld');
    });

    test('SnakeCase class', () => {
      const snake = new SnakeCase('hello world');
      expect(snake.toString()).toBe('hello_world');

      const snake2 = new SnakeCase('testCase');
      expect(snake2.toString()).toBe('test_case');
    });

    test('CamelCase class', () => {
      const camel = new CamelCase('hello world');
      expect(camel.toString()).toBe('helloWorld');

      const camel2 = new CamelCase('test-case');
      expect(camel2.toString()).toBe('testCase');
    });

    test('PascalCase class', () => {
      const pascal = new PascalCase('hello world');
      expect(pascal.toString()).toBe('HelloWorld');

      const pascal2 = new PascalCase('test-case');
      expect(pascal2.toString()).toBe('TestCase');
    });

    test('KebabCase class', () => {
      const kebab = new KebabCase('hello world');
      expect(kebab.toString()).toBe('hello-world');

      const kebab2 = new KebabCase('testCase');
      expect(kebab2.toString()).toBe('test-case');
    });

    test('UpperCase class', () => {
      const upper = new UpperCase('hello world');
      expect(upper.toString()).toBe('HELLO WORLD');
    });

    test('LowerCase class', () => {
      const lower = new LowerCase('HELLO WORLD');
      expect(lower.toString()).toBe('hello world');
    });

    test('TitleCase class', () => {
      const title = new TitleCase('hello world');
      expect(title.toString()).toBe('Hello World');
    });

    test('SentenceCase class', () => {
      const sentence = new SentenceCase('hello world');
      expect(sentence.toString()).toBe('Hello world');
    });

    test('DotCase class', () => {
      const dot = new DotCase('hello world');
      expect(dot.toString()).toBe('hello.world');
    });

    test('SpaceCase class', () => {
      const space = new SpaceCase('hello_world');
      expect(space.toString()).toBe('hello world');
    });

    test('FlatCase class', () => {
      const flat = new FlatCase('hello world');
      expect(flat.toString()).toBe('helloworld');
    });

    test('HttpHeaderCase class', () => {
      const header = new HttpHeaderCase('content-type');
      expect(header.toString()).toBe('Content-Type');
    });

    test('CamelSnakeCase class', () => {
      const camelSnake = new CamelSnakeCase('hello world');
      expect(camelSnake.toString()).toBe('hello_world');
    });

    test('HungarianCase class', () => {
      const hungarian = new HungarianCase('strUserName');
      expect(hungarian.toString()).toBe('strUserName');

      const hungarian2 = new HungarianCase('hello world');
      expect(hungarian2.toString()).toBe('helloWorld');
    });

    test('MacroCase class', () => {
      const macro = new MacroCase('hello world');
      expect(macro.toString()).toBe('HELLO_WORLD');
    });

    test('PascalSnakeCase class', () => {
      const pascalSnake = new PascalSnakeCase('hello world');
      expect(pascalSnake.toString()).toBe('Hello_World');
    });

    test('PathCase class', () => {
      const path = new PathCase('api/users');
      expect(path.toString()).toBe('api/users');
    });

    test('SlashTitleCase class', () => {
      const slashTitle = new SlashTitleCase('hello/world');
      expect(slashTitle.toString()).toBe('Hello/World');
    });
  });
}
