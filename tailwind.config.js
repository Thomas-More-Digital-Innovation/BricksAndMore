/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./voting/templates/voting/*.html",
    "./voting/templates/voting/components/*.html",
  ],
  theme:
  {
    extend: {
      scale: {
        '200': '2.00',
      }
    }
  },
  plugins: [],
}