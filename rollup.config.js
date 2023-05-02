import resolve from '@rollup/plugin-node-resolve';
import replace from '@rollup/plugin-replace';

import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';

// `npm run build` -> `production` is true
// `npm run dev` -> `production` is false
const production = !process.env.ROLLUP_WATCH;

export default [
  {
    input: '_javascript/streetnoise.js',
    output: {
      file: 'streetnoise/static/js/streetnoise.js',
      format: 'iife', // immediately-invoked function expression — suitable for <script> tags
      sourcemap: true
    },
    plugins: [
      resolve(), // tells Rollup how to find date-fns in node_modules
      commonjs(), // converts date-fns to ES modules
      production && terser() // minify, but only in production
    ]
  },
  {
    input: '_javascript/crowdfunding.js',
    output: {
      file: 'streetnoise/static/js/crowdfunding.js',
      format: 'iife', // immediately-invoked function expression — suitable for <script> tags
      sourcemap: true
    },
    plugins: [
      resolve(), // tells Rollup how to find date-fns in node_modules
      commonjs(), // converts date-fns to ES modules
      replace({
        'process.env.NODE_ENV': JSON.stringify('development'),
      }),
      production && terser() // minify, but only in production
    ]
  }
];
