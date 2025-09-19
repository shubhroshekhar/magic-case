#!/usr/bin/env node

import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
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
} from './index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Read package.json for version info
const packageJson = JSON.parse(readFileSync(join(__dirname, 'package.json'), 'utf8'));

const caseFunctions = {
  'upper': toUpperCase,
  'lower': toLowerCase,
  'camel': toCamelCase,
  'pascal': toPascalCase,
  'snake': toSnakeCase,
  'kebab': toKebabCase,
  'title': toTitleCase,
  'sentence': toSentenceCase,
  'dot': toDotCase,
  'space': toSpaceCase,
  'flat': toFlatCase,
  'http-header': toHttpHeaderCase,
  'camel-snake': toCamelSnakeCase,
  'hungarian': toHungarianCase,
  'macro': toMacroCase,
  'pascal-snake': toPascalSnakeCase,
  'path': toPathCase,
  'slash-title': toSlashTitleCase,
};

function showHelp() {
  console.log(`
magic-case v${packageJson.version}

Usage: magic-case <case-type> <text>

Available case types:
  upper          UPPERCASE
  lower          lowercase
  camel          camelCase
  pascal         PascalCase
  snake          snake_case
  kebab          kebab-case
  title          Title Case
  sentence       Sentence case
  dot            dot.case
  space          space case
  flat           flatcase
  http-header    HTTP-Header-Case
  camel-snake    camel_snake_case
  hungarian      HungarianCase
  macro          MACRO_CASE
  pascal-snake   Pascal_Snake_Case
  path           path/case
  slash-title    Slash/Title/Case

Examples:
  magic-case camel "hello world"        # helloWorld
  magic-case snake "camelCase"          # camel_case
  magic-case kebab "PascalCase"         # pascal-case
  magic-case title "hello world"        # Hello World

Options:
  -h, --help     Show this help message
  -v, --version  Show version number
`);
}

function showVersion() {
  console.log(`magic-case v${packageJson.version}`);
}

function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes('-h') || args.includes('--help')) {
    showHelp();
    return;
  }

  if (args.includes('-v') || args.includes('--version')) {
    showVersion();
    return;
  }

  if (args.length < 2) {
    console.error('❌ Error: Please provide both case type and text');
    console.error('Use --help for usage information');
    process.exit(1);
  }

  const [caseType, ...textParts] = args;
  const text = textParts.join(' ');

  if (!caseFunctions[caseType]) {
    console.error(`❌ Error: Unknown case type "${caseType}"`);
    console.error('Use --help to see available case types');
    process.exit(1);
  }

  try {
    const result = caseFunctions[caseType](text);
    console.log(result);
  } catch (error) {
    console.error(`❌ Error: ${error.message}`);
    process.exit(1);
  }
}

main();
