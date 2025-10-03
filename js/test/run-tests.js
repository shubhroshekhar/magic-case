#!/usr/bin/env node

import { readFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Simple test runner
class TestRunner {
  constructor() {
    this.tests = [];
    this.passed = 0;
    this.failed = 0;
  }

  test(name, fn) {
    // Execute tests immediately so assertions run and counters update
    try {
      const result = fn();
      // Support async tests
      if (result && typeof result.then === 'function') {
        return result.then(() => {
          // Per-assertion counters are updated in expect()
          console.log(`  ✅ ${name}`);
        }).catch((error) => {
          console.log(`  ❌ ${name}: ${error.message}`);
          this.failed++;
        });
      }
      console.log(`  ✅ ${name}`);
    } catch (error) {
      console.log(`  ❌ ${name}: ${error.message}`);
      this.failed++;
    }
  }

  describe(name, fn) {
    console.log(`\n📁 ${name}`);
    const maybePromise = fn();
    return maybePromise;
  }

  expect(actual) {
    return {
      toBe: (expected) => {
        if (actual === expected) {
          console.log(`  ✅ ${actual} === ${expected}`);
          this.passed++;
        } else {
          console.log(`  ❌ Expected ${expected}, got ${actual}`);
          this.failed++;
        }
      },
      toEqual: (expected) => {
        const pass = JSON.stringify(actual) === JSON.stringify(expected);
        if (pass) {
          console.log(`  ✅ ${JSON.stringify(actual)} == ${JSON.stringify(expected)}`);
          this.passed++;
        } else {
          console.log(`  ❌ Expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
          this.failed++;
        }
      },
      toThrow: (expectedError) => {
        try {
          actual();
          console.log(`  ❌ Expected function to throw, but it didn't`);
          this.failed++;
        } catch (error) {
          if (expectedError && !error.message.includes(expectedError)) {
            console.log(`  ❌ Expected error containing "${expectedError}", got "${error.message}"`);
            this.failed++;
          } else {
            console.log(`  ✅ Function threw as expected: ${error.message}`);
            this.passed++;
          }
        }
      },
      not: {
        toThrow: () => {
          try {
            actual();
            console.log(`  ✅ Function did not throw as expected`);
            this.passed++;
          } catch (error) {
            console.log(`  ❌ Expected function not to throw, but it threw: ${error.message}`);
            this.failed++;
          }
        }
      }
    };
  }

  async run() {
    console.log('🧪 Running magic-case tests...\n');

    // Load all test files
    const testDir = join(__dirname);
    const testFiles = readdirSync(testDir).filter(file => file.endsWith('.test.js') && file !== 'run-tests.js');

    for (const file of testFiles) {
      console.log(`\n📄 Running ${file}...`);
      const testModule = await import(join(testDir, file));
      
      // Run the tests in the module
      if (testModule.default) {
        await testModule.default();
      }
      
      // Also run any exported functions that might be tests
      for (const [name, fn] of Object.entries(testModule)) {
        if (typeof fn === 'function' && name !== 'default') {
          try {
            await fn();
          } catch (error) {
            console.log(`  ❌ Error in ${name}: ${error.message}`);
            this.failed++;
          }
        }
      }
    }

    console.log(`\n📊 Test Results:`);
    console.log(`  ✅ Passed: ${this.passed}`);
    console.log(`  ❌ Failed: ${this.failed}`);
    console.log(`  📈 Total: ${this.passed + this.failed}`);

    if (this.failed > 0) {
      process.exit(1);
    } else {
      console.log('\n🎉 All tests passed!');
    }
  }
}

// Make the test runner available globally
global.test = (name, fn) => testRunner.test(name, fn);
global.describe = (name, fn) => testRunner.describe(name, fn);
global.expect = (actual) => testRunner.expect(actual);

const testRunner = new TestRunner();

// Run the tests
testRunner.run().catch(console.error);
