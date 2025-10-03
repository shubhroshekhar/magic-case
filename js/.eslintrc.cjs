module.exports = {
  env: {
    es2022: true,
    node: true,
  },
  extends: ['eslint:recommended'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  rules: {
    'no-unused-vars': 'error',
    'no-console': 'off',
    'prefer-const': 'error',
    'no-var': 'error',
  },
  overrides: [
    {
      files: ['test/**/*.js'],
      env: { node: true },
      globals: {
        test: 'readonly',
        describe: 'readonly',
        expect: 'readonly',
      },
      rules: {
        'no-unused-vars': 'off',
      },
    },
  ],
};
