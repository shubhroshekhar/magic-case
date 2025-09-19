/**
 * Base class for all case transformers
 */
class BaseCase {
  constructor(textOrObj) {
    if (typeof textOrObj === 'string') {
      this.words = this._splitIntoWords(textOrObj);
    } else if (textOrObj instanceof BaseCase) {
      this.words = textOrObj.words;
    } else {
      throw new TypeError('BaseCase expects a string or another BaseCase instance');
    }

    if (!this.words.every(word => typeof word === 'string')) {
      throw new Error('All words must be strings');
    }
  }

  _splitIntoWords(text) {
    throw new Error('_splitIntoWords must be implemented by subclass');
  }

  toString() {
    throw new Error('toString must be implemented by subclass');
  }

  get() {
    return this.toString();
  }
}

/**
 * Convert string to UPPERCASE
 */
class UpperCase extends BaseCase {
  _splitIntoWords(text) {
    return text.toLowerCase().split(' ');
  }

  toString() {
    return this.words.join(' ').toUpperCase();
  }
}

/**
 * Convert string to lowercase
 */
class LowerCase extends BaseCase {
  _splitIntoWords(text) {
    return text.toLowerCase().split(' ');
  }

  toString() {
    return this.words.join(' ').toLowerCase();
  }
}

/**
 * Convert string to camelCase
 */
class CamelCase extends BaseCase {
  _splitIntoWords(text) {
    if (!text) {
      throw new Error('Input cannot be empty');
    }

    // Split on common separators: underscore, hyphen, dot, slash, backslash, space
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    if (this.words.length === 0) return '';
    const [first, ...rest] = this.words;
    return first.toLowerCase() + rest.map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join('');
  }
}

/**
 * Convert string to PascalCase
 */
class PascalCase extends BaseCase {
  _splitIntoWords(text) {
    // Split on common separators: underscore, hyphen, dot, slash, backslash, space
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('');
  }
}

/**
 * Convert string to snake_case
 */
class SnakeCase extends BaseCase {
  _splitIntoWords(text) {
    // Split on common separators: underscore, hyphen, dot, slash, backslash, space
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.join('_').toLowerCase();
  }
}

/**
 * Convert string to kebab-case
 */
class KebabCase extends BaseCase {
  _splitIntoWords(text) {
    // Split on common separators: underscore, hyphen, dot, slash, backslash, space
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.join('-').toLowerCase();
  }
}

/**
 * Convert string to Title Case
 */
class TitleCase extends BaseCase {
  _splitIntoWords(text) {
    return text.toLowerCase().split(' ');
  }

  toString() {
    return this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(' ');
  }
}

/**
 * Convert string to Sentence case
 */
class SentenceCase extends BaseCase {
  _splitIntoWords(text) {
    return text.toLowerCase().split(' ');
  }

  toString() {
    const sentence = this.words.join(' ');
    return sentence.charAt(0).toUpperCase() + sentence.slice(1).toLowerCase();
  }
}

/**
 * Convert string to dot.case
 */
class DotCase extends BaseCase {
  _splitIntoWords(text) {
    return text.toLowerCase().split('.');
  }

  toString() {
    return this.words.join('.').toLowerCase();
  }
}

/**
 * Convert string to space case
 */
class SpaceCase extends BaseCase {
  _splitIntoWords(text) {
    const words = text.split(' ');
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.join(' ');
  }
}

/**
 * Convert string to flatcase
 */
class FlatCase extends BaseCase {
  _splitIntoWords(text) {
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.join('');
  }
}

/**
 * Convert string to HTTP-Header-Case
 */
class HttpHeaderCase extends BaseCase {
  _splitIntoWords(text) {
    if (!text) {
      throw new Error('Input cannot be empty');
    }

    // Must strictly match: Word-Word-Word (each Word starts uppercase, then lowercase/digits)
    if (!/^(?:[A-Z][a-z0-9]*)(?:-[A-Z][a-z0-9]*)*$/.test(text)) {
      throw new Error(`Invalid HttpHeaderCase string: ${text}`);
    }

    return text.split('-');
  }

  toString() {
    return this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('-');
  }
}

/**
 * Convert string to camel_snake_case
 */
class CamelSnakeCase extends BaseCase {
  _splitIntoWords(text) {
    // Split on underscores or camel humps
    const words = text.replace(/_/g, ' ').match(/[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])/g) || [];
    return words.filter(word => word).map(word => word.toLowerCase());
  }

  toString() {
    if (this.words.length === 0) return '';
    const first = this.words[0].toLowerCase();
    const rest = this.words.slice(1).map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase());
    return [first, ...rest].join('_');
  }
}

/**
 * Convert string to Hungarian notation
 */
class HungarianCase extends BaseCase {
  constructor(textOrObj) {
    this.prefix = null;
    super(textOrObj);
  }

  _splitIntoWords(text) {
    const HUNGARIAN_PREFIXES = ['str', 'lst', 'arr', 'psz', 'i', 'b', 'd', 'f', 'ch', 'n', 'p'];
    
    // Detect Hungarian prefix
    this.prefix = null;
    for (const prefix of HUNGARIAN_PREFIXES.sort((a, b) => b.length - a.length)) {
      if (text.startsWith(prefix)) {
        this.prefix = prefix;
        text = text.slice(prefix.length);
        break;
      }
    }

    // Now split CamelCase / PascalCase
    const words = text.replace(/([a-z0-9])([A-Z])/g, '$1 $2').split(/\s+/);
    return words.filter(word => word).map(word => word.toLowerCase());
  }

  toString() {
    if (this.words.length === 0) return '';

    if (this.prefix) {
      return this.prefix + this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('');
    }

    const [first, ...rest] = this.words;
    return first + rest.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('');
  }
}

/**
 * Convert string to MACRO_CASE
 */
class MacroCase extends BaseCase {
  _splitIntoWords(text) {
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.join('_').toUpperCase();
  }
}

/**
 * Convert string to Pascal_Snake_Case
 */
class PascalSnakeCase extends BaseCase {
  _splitIntoWords(text) {
    const words = text.split(/[_\-\.,\/\\\s]+/);
    return words.filter(word => word.trim()).map(word => word.toLowerCase());
  }

  toString() {
    return this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('_');
  }
}

/**
 * Convert string to path/case
 */
class PathCase extends BaseCase {
  _splitIntoWords(text) {
    // Must strictly match: lowercase words separated by /
    if (!/^(?:[a-z0-9]+)(?:\/[a-z0-9]+)*$/.test(text)) {
      throw new Error(`Invalid PathCase string: ${text}`);
    }

    return text.split('/');
  }

  toString() {
    return this.words.join('/');
  }
}

/**
 * Convert string to Slash/Title/Case
 */
class SlashTitleCase extends BaseCase {
  _splitIntoWords(text) {
    if (!text) {
      throw new Error('Input cannot be empty');
    }

    if (text.startsWith('/') || text.endsWith('/')) {
      throw new Error(`Invalid SlashTitleCase: cannot start or end with slash → ${text}`);
    }

    const words = text.split('/');

    // Check for consecutive slashes → empty segments
    if (words.some(word => !word.trim())) {
      throw new Error(`Invalid SlashTitleCase: consecutive slashes not allowed → ${text}`);
    }

    return words;
  }

  toString() {
    return this.words.map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('/');
  }
}

// Export all classes


// Convenience functions for direct usage
function toUpperCase(text) {
  return new UpperCase(text).toString();
}

function toLowerCase(text) {
  return new LowerCase(text).toString();
}

function toCamelCase(text) {
  return new CamelCase(text).toString();
}

function toPascalCase(text) {
  return new PascalCase(text).toString();
}

function toSnakeCase(text) {
  return new SnakeCase(text).toString();
}

function toKebabCase(text) {
  return new KebabCase(text).toString();
}

function toTitleCase(text) {
  return new TitleCase(text).toString();
}

function toSentenceCase(text) {
  return new SentenceCase(text).toString();
}

function toDotCase(text) {
  return new DotCase(text).toString();
}

function toSpaceCase(text) {
  return new SpaceCase(text).toString();
}

function toFlatCase(text) {
  return new FlatCase(text).toString();
}

function toHttpHeaderCase(text) {
  return new HttpHeaderCase(text).toString();
}

function toCamelSnakeCase(text) {
  return new CamelSnakeCase(text).toString();
}

function toHungarianCase(text) {
  return new HungarianCase(text).toString();
}

function toMacroCase(text) {
  return new MacroCase(text).toString();
}

function toPascalSnakeCase(text) {
  return new PascalSnakeCase(text).toString();
}

function toPathCase(text) {
  return new PathCase(text).toString();
}

function toSlashTitleCase(text) {
  return new SlashTitleCase(text).toString();
}


// CommonJS exports
module.exports = {
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
};
