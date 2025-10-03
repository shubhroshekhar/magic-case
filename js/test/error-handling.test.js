// Test file for error handling
import {
  CamelCase,
  HttpHeaderCase,
  PathCase,
  SlashTitleCase,
  BaseCase,
} from '../index.js';

export default function runErrorTests() {
  describe('Error Handling', () => {
  test('BaseCase type validation', () => {
    expect(() => new BaseCase(123)).toThrow('BaseCase expects a string or another BaseCase instance');
    expect(() => new BaseCase(null)).toThrow('BaseCase expects a string or another BaseCase instance');
    expect(() => new BaseCase(undefined)).toThrow('BaseCase expects a string or another BaseCase instance');
  });

  test('CamelCase validation', () => {
    expect(() => new CamelCase('')).toThrow('Input cannot be empty');
    // Class now normalizes any input; invalid-start assertion removed
  });

  test('HttpHeaderCase validation', () => {
    expect(() => new HttpHeaderCase('')).toThrow('Input cannot be empty');
    // We accept lowercase/header strings and normalize on output
    expect(() => new HttpHeaderCase('invalid-header')).not.toThrow();
    expect(() => new HttpHeaderCase('content_type')).toThrow('');
    expect(() => new HttpHeaderCase('Content-Type')).not.toThrow();
  });

  test('PathCase validation', () => {
    expect(() => new PathCase('Invalid/Path')).toThrow('Invalid PathCase string');
    expect(() => new PathCase('API/Users')).toThrow('Invalid PathCase string');
    expect(() => new PathCase('api/users')).not.toThrow();
    expect(() => new PathCase('api/v1/users')).not.toThrow();
  });

  test('SlashTitleCase validation', () => {
    expect(() => new SlashTitleCase('')).toThrow('Input cannot be empty');
    expect(() => new SlashTitleCase('/hello/world')).toThrow('Invalid SlashTitleCase: cannot start or end with slash');
    expect(() => new SlashTitleCase('hello/world/')).toThrow('Invalid SlashTitleCase: cannot start or end with slash');
    expect(() => new SlashTitleCase('hello//world')).toThrow('Invalid SlashTitleCase: consecutive slashes not allowed');
    expect(() => new SlashTitleCase('hello/world')).not.toThrow();
  });

  test('Function parameter validation', async () => {
    const { toCamelCase, toHttpHeaderCase, toPathCase, toSlashTitleCase } = await import('../index.js');
    
    expect(() => toCamelCase('')).toThrow('Input cannot be empty');
    expect(() => toCamelCase('PascalCase')).not.toThrow();
    expect(() => toHttpHeaderCase('')).toThrow('Input cannot be empty');
    expect(() => toPathCase('Invalid/Path')).toThrow('Invalid PathCase string');
    expect(() => toSlashTitleCase('')).toThrow('Input cannot be empty');
  });
  });
}
