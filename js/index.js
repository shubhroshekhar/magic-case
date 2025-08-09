/**
 * Convert string to UPPERCASE
 */
export function toUpperCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text.toUpperCase();
}

/**
 * Convert string to lowercase
 */
export function toLowerCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text.toLowerCase();
}

/**
 * Convert string to camelCase
 */
export function toCamelCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text
    .toLowerCase()
    .replace(/[^a-zA-Z0-9]+(.)/g, (_, chr) => chr.toUpperCase());
}

/**
 * Convert string to PascalCase
 */
export function toPascalCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text
    .replace(/(^\w|[^a-zA-Z0-9]+\w)/g, match =>
      match.replace(/[^a-zA-Z0-9]+/, '').toUpperCase()
    );
}

/**
 * Convert string to snake_case
 */
export function toSnakeCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text
    .replace(/([a-z])([A-Z])/g, '$1_$2')
    .replace(/[^a-zA-Z0-9]+/g, '_')
    .toLowerCase();
}

/**
 * Convert string to kebab-case
 */
export function toKebabCase(text) {
  if (typeof text !== 'string') throw new TypeError('Input must be a string');
  return text
    .replace(/([a-z])([A-Z])/g, '$1-$2')
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .toLowerCase();
}
