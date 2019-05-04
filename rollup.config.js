import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';
import babel from 'rollup-plugin-babel';

export default {
  input: '_javascript/streetnoise.js',
  output: {
    file: 'streetnoise/static/js/streetnoise.js',
    format: 'cjs'
  },
  plugins: [
    resolve({
    }),
    babel({
      exclude: 'node_modules/**', // only transpile our source code
      runtimeHelpers: true,
      plugins: [
        [
          '@babel/transform-runtime',
          { useESModules: false }
        ]
      ]
    }),
    commonjs()
  ]
};
