#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const rootDir = join(__dirname, '..');

console.log('🔨 Building magic-case...');

// Read the ES module version
const esModuleContent = readFileSync(join(rootDir, 'index.js'), 'utf8');

// Convert to CommonJS
const commonJsContent = esModuleContent
  .replace(/export class/g, 'class')
  .replace(/export function/g, 'function')
  .replace(/export \{[^}]+\};/g, '')
  .replace(/export \{[^}]+\}/g, '')
  + `

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
`;

// Write CommonJS version
writeFileSync(join(rootDir, 'index.cjs'), commonJsContent);

console.log('✅ Build completed successfully!');
console.log('📦 Generated files:');
console.log('  - index.js (ES modules)');
console.log('  - index.cjs (CommonJS)');
