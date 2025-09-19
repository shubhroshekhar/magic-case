#!/usr/bin/env node

import { execSync } from 'child_process';
import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const rootDir = join(__dirname, '..');

console.log('🚀 Releasing magic-case...');

// Read current version
const packageJson = JSON.parse(readFileSync(join(rootDir, 'package.json'), 'utf8'));
const currentVersion = packageJson.version;

console.log(`Current version: ${currentVersion}`);

// Get new version from command line argument
const newVersion = process.argv[2];
if (!newVersion) {
  console.error('❌ Please provide a version number (e.g., 1.0.0)');
  process.exit(1);
}

// Validate version format
if (!/^\d+\.\d+\.\d+$/.test(newVersion)) {
  console.error('❌ Invalid version format. Use semantic versioning (e.g., 1.0.0)');
  process.exit(1);
}

console.log(`New version: ${newVersion}`);

try {
  // Update package.json version
  console.log('📝 Updating package.json...');
  packageJson.version = newVersion;
  require('fs').writeFileSync(
    join(rootDir, 'package.json'),
    JSON.stringify(packageJson, null, 2) + '\n'
  );

  // Build the package
  console.log('🔨 Building package...');
  execSync('npm run build', { cwd: rootDir, stdio: 'inherit' });

  // Run tests
  console.log('🧪 Running tests...');
  execSync('npm test', { cwd: rootDir, stdio: 'inherit' });

  // Create git tag
  console.log('🏷️  Creating git tag...');
  execSync(`git add .`, { cwd: rootDir, stdio: 'inherit' });
  execSync(`git commit -m "Release v${newVersion}"`, { cwd: rootDir, stdio: 'inherit' });
  execSync(`git tag v${newVersion}`, { cwd: rootDir, stdio: 'inherit' });

  // Publish to npm
  console.log('📦 Publishing to npm...');
  execSync('npm publish', { cwd: rootDir, stdio: 'inherit' });

  // Push to git
  console.log('📤 Pushing to git...');
  execSync('git push origin main', { cwd: rootDir, stdio: 'inherit' });
  execSync(`git push origin v${newVersion}`, { cwd: rootDir, stdio: 'inherit' });

  console.log('✅ Release completed successfully!');
  console.log(`🎉 magic-case v${newVersion} is now available on npm!`);

} catch (error) {
  console.error('❌ Release failed:', error.message);
  process.exit(1);
}
