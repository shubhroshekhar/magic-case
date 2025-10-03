/**
 * Base class for all case transformers
 */
class BaseCase {
  constructor(textOrObj) {
    if (typeof textOrObj === 'string') {
      this.words = this._splitIntoWords(textOrObj);
    } else if (textOrObj instanceof BaseCase) {
      // Re-parse from the string form to adapt to the target case's splitter
      this.words = this._splitIntoWords(textOrObj.toString());
    } else {
      throw new TypeError('BaseCase expects a string or another BaseCase instance');
    }

    if (!this.words.every(word => typeof word === 'string')) {
      throw new Error('All words must be strings');
    }
  }

  _splitIntoWords() {
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
    // Accept any input and normalize
    const normalized = text
      .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
      .replace(/[-_.\s]+|\/+/g, ' ');
    return normalized.split(' ').filter(Boolean).map(w => w.toLowerCase());
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
    const normalized = text
      .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
      .replace(/[-_.\s]+|\/+/g, ' ');
    return normalized.split(' ').filter(Boolean).map(w => w.toLowerCase());
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
    const snake = String(text)
      .replace(/([a-z0-9])([A-Z])/g, '$1_$2')
      .replace(/[^a-zA-Z0-9]+/g, '_')
      .replace(/_+/g, '_')
      .toLowerCase();
    return [snake];
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
    const normalized = text.replace(/[_.\s]+|\/+/g, ' ');
    const parts = (normalized.match(/[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])/g) || []);
    return parts.map(w => w.toLowerCase());
  }

  toString() {
    const combined = this.words.join(' ');
    return combined
      .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
      .replace(/[^a-zA-Z0-9]+/g, '-')
      .replace(/-+/g, '-')
      .toLowerCase();
  }
}

/**
 * Convert string to Title Case
 */
class TitleCase extends BaseCase {
  _splitIntoWords(text) {
    // Not used for transformation; TitleCase preserves original separators
    return [text];
  }

  toString() {
    const original = this.words[0] || '';
    return String(original).replace(/[A-Za-z0-9]+/g, (word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase());
  }
}

/**
 * Convert string to Sentence case
 */
class SentenceCase extends BaseCase {
  _splitIntoWords(text) {
    return [text];
  }

  toString() {
    const lower = String(this.words[0] || '').toLowerCase();
    return lower.replace(/[a-zA-Z]/, (m) => m.toUpperCase());
  }
}

/**
 * Convert string to dot.case
 */
class DotCase extends BaseCase {
  _splitIntoWords(text) {
    const normalized = text
      .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
      .replace(/[-_.\s]+|\/+/g, ' ');
    return normalized.split(' ').filter(Boolean).map(w => w.toLowerCase());
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
    const normalized = text
      .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
      .replace(/[-_.\s]+|\/+/g, ' ');
    return normalized.split(' ').filter(Boolean).map(w => w.toLowerCase());
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
      const words = text.split(/[._\s-]+|\/+/);
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
    if (text.includes('_')) {
      throw new Error('Invalid HttpHeaderCase string');
    }
    return text.split(/-+/);
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
    return this.words.join('_');
  }
}

/**
 * Convert string to Hungarian notation
 */
class HungarianCase extends BaseCase {
  constructor(textOrObj) {
    // Initialize before parsing so _splitIntoWords can set it
    super(textOrObj);
    if (this.prefix === undefined) this.prefix = null;
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
    const words = text.split(/[._\s-]+|\/+/);
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
    const words = text.split(/[._\s-]+|\/+/);
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
export {
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
};

// Convenience functions for direct usage
export function toUpperCase(text) {
  return new UpperCase(text).toString();
}

export function toLowerCase(text) {
  return new LowerCase(text).toString();
}

export function toCamelCase(text) {
  return new CamelCase(text).toString();
}

export function toPascalCase(text) {
  return new PascalCase(text).toString();
}

export function toSnakeCase(text) {
  return new SnakeCase(text).toString();
}

export function toKebabCase(text) {
  return new KebabCase(text).toString();
}

export function toTitleCase(text) {
  return new TitleCase(text).toString();
}

export function toSentenceCase(text) {
  return new SentenceCase(text).toString();
}

export function toDotCase(text) {
  return new DotCase(text).toString();
}

export function toSpaceCase(text) {
  return new SpaceCase(text).toString();
}

export function toFlatCase(text) {
  return new FlatCase(text).toString();
}

export function toHttpHeaderCase(text) {
  return new HttpHeaderCase(text).toString();
}

export function toCamelSnakeCase(text) {
  return new CamelSnakeCase(text).toString();
}

export function toHungarianCase(text) {
  return new HungarianCase(text).toString();
}

export function toMacroCase(text) {
  return new MacroCase(text).toString();
}

export function toPascalSnakeCase(text) {
  return new PascalSnakeCase(text).toString();
}

export function toPathCase(text) {
  return new PathCase(text).toString();
}

export function toSlashTitleCase(text) {
  return new SlashTitleCase(text).toString();
}
